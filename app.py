from flask import Flask, render_template, jsonify
import psutil
from ping3 import ping
import sqlite3, datetime

app = Flask(__name__)
DB_PATH = "logs.db"

# إنشاء قاعدة البيانات إذا ما كانت موجودة
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (time TEXT, server TEXT, cpu REAL, memory REAL, disk REAL, status TEXT)''')
    conn.commit()
    conn.close()

init_db()

def get_server_data():
    servers = ["8.8.8.8", "example.com"]
    data = []
    for s in servers:
        response = ping(s, timeout=2)
        status = "Healthy" if response else "Down"
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        # حفظ النتيجة في قاعدة البيانات
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO logs VALUES (?, ?, ?, ?, ?, ?)",
                  (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), s, cpu, mem, disk, status))
        conn.commit()
        conn.close()

        data.append({
            "server": s,
            "cpu": cpu,
            "memory": mem,
            "disk": disk,
            "ping": round(response*1000, 2) if response else None,
            "status": status
        })
    return data

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/status')
def api_status():
    return jsonify(get_server_data())

@app.route('/api/logs')
def api_logs():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY time DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return jsonify([
        {"time": r[0], "server": r[1], "cpu": r[2], "memory": r[3], "disk": r[4], "status": r[5]}
        for r in rows
    ])

if __name__ == "__main__":
    app.run(debug=True)
