import sqlite3

conn = sqlite3.connect("firewall.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS rules (
id INTEGER PRIMARY KEY,
ip TEXT,
port TEXT,
action TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
id INTEGER PRIMARY KEY,
event TEXT
)
""")

conn.commit()
conn.close()
print("Database created successfully")
