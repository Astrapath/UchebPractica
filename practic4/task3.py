import psutil
import sqlite3
import time


def db():
    conn = sqlite3.connect('sysmonitor.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS monitoring (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATATIME 
    DEFAULT CURRENT_TIMESTAMP, cpu REAL, memory REAL, disk REAL)''')
    conn.commit()
    conn.close()


def sysstats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk


def save(cpu, memory, disk):
    conn = sqlite3.connect('sysmonitor.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO monitoring (cpu, memory, disk) VALUES (?, ?, ?) ''', (cpu, memory, disk))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('sysmonitor.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM monitoring")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()


db()
try:
    while True:
        cpu, memory, disk = sysstats()
        save(cpu, memory, disk)
        print(f'CPU: {cpu}%, память: {memory}%, диск: {disk}%')
        time.sleep(30)
except KeyboardInterrupt:
    print('монтиторинг остановлен, данные сохранены')
    view()
