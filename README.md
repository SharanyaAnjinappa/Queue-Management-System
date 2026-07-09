# Queue Management System

A web-based **Queue Management System** that enables managers to create and manage multiple service queues, generate queue-specific tokens, serve customers efficiently, and monitor queue performance through an interactive analytics dashboard.

---

# Overview

Queue Management System is a web-based application developed to simplify the management of customer queues in environments such as hospitals, banks, clinics, and service centers.

The system allows managers to:

- Create multiple queues
- Generate automatic tokens
- Manage waiting customers
- Reorder tokens
- Serve customers
- Monitor queue statistics through an interactive dashboard

The application provides queue-specific token management, activity tracking, graphical analytics, and an intuitive user interface to improve service efficiency and reduce customer waiting time.

---

# Features

## 🔐 Authentication

- Secure Manager Login
- Invalid login message displayed on the login page

## 📋 Queue Management

- Create Multiple Queues
- Delete Existing Queues
- Queue Description Support
- Independent Queue Management

## 🎟️ Token Management

- Automatic Queue-Specific Token Generation (T001, T002...)
- Add Customers with Name and Phone Number
- Queue-Specific Waiting Lists
- Serve Next Customer
- Cancel Tokens
- Move Tokens Up or Down in the Queue
- Displays Currently Serving Token

## 📊 Dashboard & Analytics

- Total Number of Queues
- Total Waiting Tokens
- Total Served Tokens
- Total Cancelled Tokens
- Average Waiting Time
- Queue-wise Statistics
- Queue Length Trend Chart
- Daily Tokens Served Chart
- Scrollable Recent Activity Log

## 📈 Activity Tracking

- Queue Creation History
- Token Creation History
- Token Served History
- Token Cancellation History

---

# Technologies Used

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chart.js

## Backend

- Python
- Flask

## Database

- SQLite

---

# Installation

## Prerequisites

- Python 3.11 or later

### Install Required Packages

```bash
pip install flask
```

or

```bash
pip install -r requirements.txt
```

---

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Queue-Management-System.git

cd Queue-Management-System
```

---

## Create Virtual Environment (Optional)

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv

source venv/bin/activate
```

---

## Create Database

```bash
python database.py
```

---

## Run the Application

```bash
python app.py
```

---

## Open in Browser

```text
http://127.0.0.1:5000/
```

---

# Default Login Credentials

```text
Username : manager
Password : admin123
```

---

# Project Workflow

1. Launch the application.
2. Login as the Queue Manager.
3. Create one or more service queues.
4. Select a queue to manage.
5. Add customers to generate automatic queue-specific tokens.
6. View the waiting list for the selected queue.
7. Reorder tokens using Move Up or Move Down.
8. Serve customers using the **Serve Next** option.
9. Cancel tokens when required.
10. Monitor queue statistics and recent activities through the dashboard.

---

# Project Structure

```text
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
```

---

# Future Enhancements

- Multi-user Authentication (Admin & Manager)
- Email/SMS Token Notifications
- QR Code-Based Token Generation
- Search and Filter Tokens
- Export Queue Reports (PDF/Excel)
- Customer Self-Service Token Generation
- Estimated Waiting Time Prediction
- Real-time Queue Display Screen
- Dashboard Analytics with Historical Reports

---

# Screenshots

Include screenshots of:

- Login Page
<img width="887" height="474" alt="image" src="https://github.com/user-attachments/assets/695f4932-bbcd-44ad-8cf8-f1f1949f7070" />

- Dashboard
<img width="760" height="419" alt="image" src="https://github.com/user-attachments/assets/c4db0913-8789-4ee5-bb94-5c4ecad1f56b" />
<img width="820" height="395" alt="image" src="https://github.com/user-attachments/assets/92dc2c48-c72e-4469-b505-cc1beaeb20a3" />


- Create Queue Page
<img width="890" height="445" alt="image" src="https://github.com/user-attachments/assets/a326520d-c7db-473f-99cb-e9c20b8fb5f4" />
<img width="894" height="464" alt="image" src="https://github.com/user-attachments/assets/e849c8cc-4e3c-49e2-83e0-d7b86c135a7e" />


- Manage Queue Page
<img width="895" height="443" alt="image" src="https://github.com/user-attachments/assets/6fda45c7-2d1b-4b6d-8400-21b96a787fcb" />
<img width="905" height="446" alt="image" src="https://github.com/user-attachments/assets/3599a030-62fd-4876-885c-8d17994518f5" />
<img width="900" height="464" alt="image" src="https://github.com/user-attachments/assets/9b87b458-bc4c-4aff-a9df-4051ee774f44" />





---

# Author

**Sharanya A**

B.Tech – Computer Science and Engineering

Dayananda Sagar University
