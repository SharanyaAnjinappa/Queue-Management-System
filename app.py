from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)


# -------------------------------
# Database Connection
# -------------------------------
def get_db():
    conn = sqlite3.connect(
        "queue.db",
        timeout=10,
        check_same_thread=False
    )

    conn.row_factory = sqlite3.Row

    return conn

# -------------------------------
# Login Page
# -------------------------------
@app.route("/")
def home():
    return render_template("login.html")


# -------------------------------
# Login
# -------------------------------
@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username == "manager" and password == "admin123":
        return redirect("/dashboard")

    return render_template(
        "login.html",
        error="Invalid Username or Password"
    )


# -------------------------------
# Dashboard
# -------------------------------
@app.route("/dashboard")
def dashboard():

    conn = get_db()
    cursor = conn.cursor()

    # -----------------------
    # Statistics
    # -----------------------

    cursor.execute("SELECT COUNT(*) FROM queues")
    total_queues = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tokens WHERE status='Waiting'")
    waiting = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tokens WHERE status='Serving'")
    serving = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tokens WHERE status='Served'")
    served = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tokens WHERE status='Cancelled'")
    cancelled = cursor.fetchone()[0]

    queue_length = waiting

    # -----------------------
    # Average Wait Time
    # -----------------------

    cursor.execute("""
        SELECT AVG(
            (strftime('%s', served_at) -
             strftime('%s', created_at))/60.0
        )
        FROM tokens
        WHERE served_at IS NOT NULL
    """)

    result = cursor.fetchone()[0]

    if result is not None:
        avg_wait = round(result)
    else:
        avg_wait = 0

    # -----------------------
    # Queue Cards
    # -----------------------

    cursor.execute("SELECT * FROM queues")

    queue_rows = cursor.fetchall()

    queues = []

    for q in queue_rows:

        qid = q["id"]

        cursor.execute("""
            SELECT COUNT(*)
            FROM tokens
            WHERE queue_id=?
            AND status='Waiting'
        """, (qid,))
        wait_count = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM tokens
            WHERE queue_id=?
            AND status='Served'
        """, (qid,))
        served_count = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM tokens
            WHERE queue_id=?
            AND status='Cancelled'
        """, (qid,))
        cancel_count = cursor.fetchone()[0]

        queues.append({

            "id": qid,
            "name": q["name"],
            "description": q["description"],
            "waiting": wait_count,
            "served": served_count,
            "cancelled": cancel_count

        })

    # -----------------------
    # Recent Activity
    # -----------------------

    cursor.execute("""
        SELECT *
        FROM activities
        ORDER BY time DESC
    """)

    activities = cursor.fetchall()

    # -----------------------
    # Chart Data
    # -----------------------

    chart_waiting = waiting
    chart_serving = serving
    chart_served = served
    chart_cancelled = cancelled

    # -----------------------
    # Daily Tokens Served
    # -----------------------

    served_data = [0, 0, 0, 0, 0, 0, 0]

    cursor.execute("""
        SELECT served_at
        FROM tokens
        WHERE status='Served'
        AND served_at IS NOT NULL
    """)

    rows = cursor.fetchall()

    for row in rows:

        dt = datetime.strptime(
            row["served_at"],
            "%Y-%m-%d %H:%M:%S"
        )

        served_data[dt.weekday()] += 1

    conn.close()

    return render_template(

        "dashboard.html",

        total_queues=total_queues,

        waiting=waiting,
        serving=serving,
        served=served,
        cancelled=cancelled,

        avg_wait=avg_wait,
        queue_length=queue_length,

        queues=queues,
        activities=activities,

        chart_waiting=chart_waiting,
        chart_serving=chart_serving,
        chart_served=chart_served,
        chart_cancelled=chart_cancelled,

        served_data=served_data

    )
# -------------------------------
# Create Queue
# -------------------------------
@app.route("/create")
def create_queue():
    return render_template("create_queue.html")


@app.route("/create", methods=["POST"])
def save_queue():

    queue_name = request.form["queue_name"]
    description = request.form["description"]

    conn = get_db()
    cursor = conn.cursor()

    # Insert Queue
    cursor.execute("""
        INSERT INTO queues(name, description)
        VALUES(?, ?)
    """, (queue_name, description))

    # Save Activity
    cursor.execute("""
        INSERT INTO activities(title, message)
        VALUES(?, ?)
    """, (
        "Queue Created",
        f"{queue_name} queue was created"
    ))

    conn.commit()
    conn.close()

    return redirect("/dashboard")

# -------------------------------
# Manage Queue
# -------------------------------
@app.route("/manage")
def manage_queue():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM queues ORDER BY id")
    queues = cursor.fetchall()

    selected_queue = request.args.get("queue_id", type=int)

    if selected_queue is None and queues:
        selected_queue = queues[0]["id"]

    tokens = []
    serving = None

    if selected_queue:

        cursor.execute("""
            SELECT *
            FROM tokens
            WHERE queue_id=?
            AND status='Waiting'
            ORDER BY position
        """, (selected_queue,))
        tokens = cursor.fetchall()

        cursor.execute("""
            SELECT *
            FROM tokens
            WHERE queue_id=?
            AND status='Serving'
            LIMIT 1
        """, (selected_queue,))
        serving = cursor.fetchone()

    conn.close()

    return render_template(
        "manage_queue.html",
        queues=queues,
        tokens=tokens,
        serving=serving,
        selected_queue=selected_queue
    )
# -------------------------------
# Add Person
# -------------------------------
@app.route("/add_person", methods=["POST"])
def add_person():

    queue_id = request.form["queue_id"]
    name = request.form["name"]
    phone = request.form["phone"]

    conn = get_db()
    cursor = conn.cursor()

    # -------------------------------
    # Generate Token Number
    # -------------------------------
    cursor.execute("""
        SELECT token
        FROM tokens
        WHERE queue_id=?
        ORDER BY id DESC
        LIMIT 1
    """, (queue_id,))

    last_token = cursor.fetchone()
    if last_token:
        token_no = int(last_token["token"][1:]) + 1
    else:
        token_no = 1
    token = f"T{token_no:03}"

    # -------------------------------
    # Queue Position
    # -------------------------------
    cursor.execute("""
        SELECT COUNT(*)
        FROM tokens
        WHERE queue_id=?
        AND status='Waiting'
    """, (queue_id,))

    position = cursor.fetchone()[0] + 1

    # -------------------------------
    # Insert Token
    # -------------------------------
    cursor.execute("""
        INSERT INTO tokens
        (
            queue_id,
            token,
            name,
            phone,
            status,
            position
        )
        VALUES
        (
            ?, ?, ?, ?, 'Waiting', ?
        )
    """,
    (
        queue_id,
        token,
        name,
        phone,
        position
    ))

    # -------------------------------
    # Save Activity
    # -------------------------------
    cursor.execute("""
        INSERT INTO activities(title, message)
        VALUES(?, ?)
    """, (
        "Token Added",
        f"{token} - {name} joined the queue"
    ))

    conn.commit()
    conn.close()

    return redirect(f"/manage?queue_id={queue_id}")


# -------------------------------
# Delete Token
# -------------------------------
@app.route("/cancel/<int:id>")
def cancel_token(id):

    conn = get_db()
    cursor = conn.cursor()

    # Get token details
    cursor.execute("""
        SELECT token, name, queue_id
        FROM tokens
        WHERE id=?
    """, (id,))

    token = cursor.fetchone()

    if token:

        queue_id = token["queue_id"]

        # Cancel the token
        cursor.execute("""
            UPDATE tokens
            SET status='Cancelled'
            WHERE id=?
        """, (id,))

        # Save activity
        cursor.execute("""
            INSERT INTO activities(title, message)
            VALUES(?, ?)
        """, (
            "Token Cancelled",
            f"{token['token']} - {token['name']} was cancelled"
        ))

        conn.commit()

    conn.close()

    return redirect(f"/manage?queue_id={queue_id}")
# -------------------------------
# Move Token Up
# -------------------------------
@app.route("/move_up/<int:id>")
def move_up(id):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tokens
        WHERE id=?
    """, (id,))

    current = cursor.fetchone()

    if current:

        cursor.execute("""
            SELECT *
            FROM tokens
            WHERE queue_id=?
            AND position < ?
            AND status='Waiting'
            ORDER BY position DESC
            LIMIT 1
        """,
        (
            current["queue_id"],
            current["position"]
        ))

        above = cursor.fetchone()

        if above:

            cursor.execute(
                "UPDATE tokens SET position=? WHERE id=?",
                (above["position"], current["id"])
            )

            cursor.execute(
                "UPDATE tokens SET position=? WHERE id=?",
                (current["position"], above["id"])
            )

            conn.commit()

    conn.close()

    return redirect(f"/manage?queue_id={current['queue_id']}")


# -------------------------------
# Move Token Down
# -------------------------------
@app.route("/move_down/<int:id>")
def move_down(id):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tokens
        WHERE id=?
    """, (id,))

    current = cursor.fetchone()

    if current:

        cursor.execute("""
            SELECT *
            FROM tokens
            WHERE queue_id=?
            AND position > ?
            AND status='Waiting'
            ORDER BY position ASC
            LIMIT 1
        """,
        (
            current["queue_id"],
            current["position"]
        ))

        below = cursor.fetchone()

        if below:

            cursor.execute(
                "UPDATE tokens SET position=? WHERE id=?",
                (below["position"], current["id"])
            )

            cursor.execute(
                "UPDATE tokens SET position=? WHERE id=?",
                (current["position"], below["id"])
            )

            conn.commit()

    conn.close()

    return redirect(f"/manage?queue_id={current['queue_id']}")


# -------------------------------
# Serve Next Token
# -------------------------------
@app.route("/serve_next/<int:queue_id>")
def serve_next(queue_id):

    conn = get_db()
    cursor = conn.cursor()

    # Finish current serving token
    cursor.execute("""
        UPDATE tokens
        SET
            status='Served',
            served_at=CURRENT_TIMESTAMP
        WHERE status='Serving'
        AND queue_id=?
    """, (queue_id,))

    # Get next waiting token
    cursor.execute("""
        SELECT *
        FROM tokens
        WHERE queue_id=?
        AND status='Waiting'
        ORDER BY position
        LIMIT 1
    """, (queue_id,))

    token = cursor.fetchone()

    if token:

        cursor.execute("""
            UPDATE tokens
            SET status='Serving'
            WHERE id=?
        """, (token["id"],))

        cursor.execute("""
            INSERT INTO activities(title, message)
            VALUES(?, ?)
        """, (
            "Token Serving",
            f"{token['token']} - {token['name']} is now being served"
        ))

    conn.commit()
    conn.close()

    return redirect(f"/manage?queue_id={queue_id}")

# -------------------------------
# Delete Queue
# -------------------------------
@app.route("/delete/<int:id>")
def delete_queue(id):

    conn = get_db()

    # Delete tokens first
    conn.execute(
        "DELETE FROM tokens WHERE queue_id=?",
        (id,)
    )

    # Delete queue
    conn.execute(
        "DELETE FROM queues WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/dashboard")


# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)