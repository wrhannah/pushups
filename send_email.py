import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

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
        server.starttls()  # Secure the connection
        server.login(BREVO_SMTP_USER, BREVO_SMTP_PASSWORD)
        server.send_message(msg)
    print("Email sent!")

if __name__ == "__main__":
    send_email()