import os
import sqlite3
from email_alert import send_alert

DB_NAME = "firewall.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS rules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        port TEXT,
        action TEXT
    )
    """)

    conn.commit()
    conn.close()

# Run init when file loads
init_db()

def add_rule(ip, port, action):

    if action == "BLOCK":
        os.system(
          f'netsh advfirewall firewall add rule name="Block {ip}" dir=in action=block remoteip={ip} protocol=TCP localport={port}'
        )
    else:
        os.system(
          f'netsh advfirewall firewall add rule name="Allow {ip}" dir=in action=allow remoteip={ip} protocol=TCP localport={port}'
        )

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO rules(ip,port,action) VALUES (?,?,?)",
                (ip,port,action))
    conn.commit()
    conn.close()
    send_alert(f"Rule Added: {ip}:{port} -> {action}")

def get_rules():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM rules")
    rows = cur.fetchall()
    conn.close()
    return rows
