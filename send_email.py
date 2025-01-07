from flask import Flask
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

BREVO_SMTP_USER = os.environ.get("BREVO_SMTP_USER")
BREVO_SMTP_PASSWORD = os.environ.get("BREVO_SMTP_PASSWORD")

def send_email():
    recipient = "nctuners@gmail.com"
    subject = "Push-Ups Time!!!!!!!"
    body = "It's time to do your push-ups!"

    msg = MIMEMultipart()
    msg["From"] = BREVO_SMTP_USER
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp-relay.brevo.com", 587) as server:
        server.starttls()
        server.login(BREVO_SMTP_USER, BREVO_SMTP_PASSWORD)
        server.send_message(msg)
    print("Email sent!")

@app.route("/")
def trigger_email():
    send_email()
    return "Email sent!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
