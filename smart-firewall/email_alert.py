import smtplib
from email.message import EmailMessage

def send_alert(message):

    EMAIL="amanranaa12@gmail.com"
    PASSWORD="hrst oinn hdif bfgs"

    msg=EmailMessage()
    msg.set_content(message)
    msg["Subject"]="Firewall Alert"
    msg["From"]=EMAIL
    msg["To"]=EMAIL

    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(EMAIL,PASSWORD)
    server.send_message(msg)
    server.quit()
