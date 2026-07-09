# Queue-Management-System
A Flask-based Queue Management System with multi-queue support, automatic token generation, queue management, analytics dashboard, and real-time activity tracking using SQLite and Chart.js

A web-based Queue Management System built using Python (Flask), SQLite, HTML, CSS, Bootstrap, and JavaScript. The system helps queue managers create and manage multiple queues efficiently by generating tokens, serving customers, tracking queue statistics, and monitoring activities through an interactive dashboard.

🚀 Features
Authentication
Secure Manager Login
Invalid login message displayed on the same login page
Dashboard
Total Queues
Waiting Tokens
Served Tokens
Cancelled Tokens
Average Waiting Time
Queue-wise Statistics
Queue Length Trend Chart
Daily Tokens Served Chart
Recent Activity Log
Queue Management
Create Multiple Queues
Delete Queues
Queue Description Support
Token Management
Automatic Token Generation (T001, T002...)
Queue-specific Token Numbering
Add Person with Name & Phone Number
Serve Next Token
Cancel Tokens
Reorder Tokens (Move Up / Move Down)
Queue-specific Waiting List
Queue-specific "Now Serving"
Activity Tracking
Queue Creation History
Token Added
Token Served
Token Cancelled
Scrollable Activity Feed

🛠️ Technologies Used
Python
Flask
SQLite
HTML5
CSS3
Bootstrap 5
JavaScript
Chart.js

📂 Project Structure
Queue-Management-System/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── create_queue.html
│   └── manage_queue.html
│
├── app.py
├── database.py
├── queue.db
├── requirements.txt
└── README.md

⚙️ Installation

Clone the repository

git clone https://github.com/yourusername/Queue-Management-System.git

Move into the project

cd Queue-Management-System

Create a virtual environment

python -m venv venv

Activate it

Windows

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Create the database

python database.py

Run the application

python app.py

Open your browser

http://127.0.0.1:5000

🔐 Default Login
Username : manager
Password : admin123

📊 Future Improvements
Role-based authentication
SMS/Email notifications
Token display screen
Customer self-registration
QR Code based token generation
Queue analytics and reports
Export reports to PDF/Excel
Search and filter tokens
Estimated waiting time prediction

📸 Screenshot
Login Page
Dashboard
Create Queue
Manage Queue
Queue Statistics

👩‍💻 Author
Sharanya A
B.Tech – Computer Science and Engineering
Dayananda Sagar University
