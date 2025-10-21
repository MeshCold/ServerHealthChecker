# Automated Server Health Checker Dashboard

This project is a Flask-based web dashboard that automatically monitors the health of servers in real time. It displays CPU, memory, and disk usage, network ping, and server status, and includes popup alerts and a log of recent checks. The system is designed for IT engineers and administrators who need a simple, efficient way to monitor servers through a browser.

The dashboard provides real-time server metrics that refresh automatically every few seconds. It records each check in an SQLite database, displays the latest ten logs, and notifies the user immediately if a server becomes unreachable. The interface uses TailwindCSS for a modern dark design.

Project structure:
server_health_checker/
├── app.py              # Flask backend with logging and alert logic
├── logs.db             # SQLite database (auto created)
├── static/
│   ├── css/
│   └── js/
└── templates/
    └── index.html      # Dashboard interface

To run the project:
1. Clone or download the repository, then navigate to the folder:
   git clone https://github.com/yourusername/server-health-checker.git
   cd server-health-checker

2. Install the required packages:
   pip install flask psutil ping3

3. Start the Flask server:
   python app.py

4. Open your browser and go to:
   http://127.0.0.1:5000

The dashboard will display all monitored servers, their resource usage, ping times, and health status. If any server goes down, a red popup alert appears on the top corner of the page, and the event is logged in the database for review. The logs section at the bottom of the page lists the latest health checks with timestamps, CPU, and memory readings for quick tracking.

Future improvements may include adding user authentication, email or Telegram notifications, trend charts for CPU and memory usage, and dynamic management of servers through the dashboard.

