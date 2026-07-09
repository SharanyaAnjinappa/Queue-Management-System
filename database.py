import sqlite3

conn = sqlite3.connect("queue.db")

cursor = conn.cursor()

# ----------------------------
# Queue Table
# ----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS queues(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
)
""")

# ----------------------------
# Token Table
# ----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS tokens(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    queue_id INTEGER,
    token TEXT,
    name TEXT,
    phone TEXT,
    status TEXT DEFAULT 'Waiting',
    position INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    served_at TIMESTAMP,
    FOREIGN KEY(queue_id) REFERENCES queues(id)
)
""")
# ----------------------------
# Activity Table
# ----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS activities(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    message TEXT,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")