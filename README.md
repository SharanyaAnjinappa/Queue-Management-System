Queue-Management-System

A web-based Queue Management System that enables managers to create and manage multiple service queues, generate queue-specific tokens, serve customers efficiently, and monitor queue performance through an interactive analytics dashboard.

Queue Management System
Overview

Queue Management System is a web-based application developed to simplify the management of customer queues in environments such as hospitals, banks, clinics, and service centers. The system allows managers to create multiple queues, generate automatic tokens, manage waiting customers, reorder tokens, serve customers, and monitor queue statistics through a real-time dashboard.

The application provides queue-specific token management, activity tracking, graphical analytics, and an intuitive user interface to improve service efficiency and reduce customer waiting time.

Features
🔐 Authentication
Secure Manager Login
Invalid login message displayed on the login page
📋 Queue Management
Create Multiple Queues
Delete Existing Queues
Queue Description Support
Independent Queue Management
🎟️ Token Management
Automatic Queue-Specific Token Generation (T001, T002...)
Add Customers with Name and Phone Number
Queue-Specific Waiting Lists
Serve Next Customer
Cancel Tokens
Move Tokens Up or Down in the Queue
Displays Currently Serving Token
📊 Dashboard & Analytics
Total Number of Queues
Total Waiting Tokens
Total Served Tokens
Total Cancelled Tokens
Average Waiting Time
Queue-wise Statistics
Queue Length Trend Chart
Daily Tokens Served Chart
Scrollable Recent Activity Log
📈 Activity Tracking
Queue Creation History
Token Creation History
Token Served History
Token Cancellation History
Technologies Used
Frontend
HTML5
CSS3
Bootstrap 5
JavaScript
Chart.js
Backend
Python
Flask
Database
SQLite
Installation
Prerequisites
Python 3.11 or later

Install the required packages

pip install flask
pip install sqlite3

or

pip install -r requirements.txt
Clone the Repository
git clone https://github.com/YOUR_USERNAME/Queue-Management-System.git

cd Queue-Management-System
Create a Virtual Environment (Optional)
Windows
python -m venv venv

venv\Scripts\activate
Linux / macOS
python -m venv venv

source venv/bin/activate
Create Database
python database.py
Run the Application
python app.py
Open in Browser
http://127.0.0.1:5000/
Default Login Credentials
Username : manager
Password : admin123
Project Workflow
Launch the application.
Login as the Queue Manager.
Create one or more service queues.
Select a queue to manage.
Add customers to generate automatic queue-specific tokens.
View the waiting list for the selected queue.
Reorder tokens using Move Up or Move Down.
Serve customers using the Serve Next option.
Cancel tokens when required.
Monitor queue statistics and recent activities through the dashboard.
Project Structure
Queue-Management-System/
│
├── static/
│   ├── css/
│   │   ├── login.css
│   │   ├── dashboard.css
│   │   ├── create_queue.css
│   │   └── manage_queue.css
│   │
│   ├── js/
│   │   └── dashboard.js
│   │
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
Future Enhancements
Multi-user Authentication (Admin & Manager)
Email/SMS Token Notifications
QR Code-Based Token Generation
Search and Filter Tokens
Export Queue Reports (PDF/Excel)
Customer Self-Service Token Generation
Estimated Waiting Time Prediction
Real-time Queue Display Screen
Dashboard Analytics with Historical Reports
Screenshots

Include screenshots of:

Login Page
Dashboard
Create Queue Page
Manage Queue Page
Queue Statistics Dashboard
Author

Sharanya A

B.Tech – Computer Science and Engineering
Dayananda Sagar University
