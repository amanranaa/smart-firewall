# 🔐 Smart Software Firewall with Web-Based Management Dashboard

A Python-based firewall system with a web interface that allows administrators to manage firewall rules, block or allow IP addresses and ports, view logs, and visualize firewall analytics.

---

## 🚀 Features
- Block / Allow IP & Port
- Web-based dashboard (Flask)
- SQLite database for rules
- Real-time analytics chart
- Email alert when rule is added
- Works on Windows Firewall & Linux iptables
  

---

## 🛠️ Technologies Used
- Python
- Flask
- SQLite
- HTML, CSS
- Chart.js
- Windows Firewall / iptables

---

## 📂 Project Structure

smart-firewall/
│
├── app.py
├── firewall.py
├── email_alert.py  
├── firewall.db  -- Auto Generated
│
├── templates/
│   ├── login.html
│   └── dashboard.html
│
└── static/
    └── style.css


## Authentication

This project uses a demo authentication mechanism for learning purposes.  
Credentials can be configured inside `app.py`.

Future Improvement: Implement hashed password authentication.

## ⚙️ Installation

```bash
pip install flask
```

## ▶️ Run Project
```bash
python app.py
```
Open in browser:
```bash
http://127.0.0.1:5000
```

## Screenshot

<img width="2184" height="1581" alt="Screenshot 2026-02-08 151841" src="https://github.com/user-attachments/assets/55102624-db9f-49f2-b5e5-8f02b670926a" />

<img width="2603" height="1003" alt="Screenshot 2026-02-08 151926" src="https://github.com/user-attachments/assets/1261c092-9938-4377-9aec-74a42885e043" />

<img width="2602" height="939" alt="Screenshot 2026-02-08 151945" src="https://github.com/user-attachments/assets/55940ebb-d7d3-4e2e-aab1-5ecbb4ab04e5" />


## 👨‍💻 Author

Aman Kumar Rana
Cybersecurity & Web Developer
