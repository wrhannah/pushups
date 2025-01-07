from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime

app = Flask(__name__)

# Environment variables for SMTP credentials
BREVO_SMTP_USER = os.environ.get("BREVO_SMTP_USER")
BREVO_SMTP_PASSWORD = os.environ.get("BREVO_SMTP_PASSWORD")

def send_email():
    recipient = "nctuners@gmail.com"
    subject = "Push-Ups Time!
    body = "Wake up! It's time to do your push-ups!"

    msg = MIMEMultipart()
    msg["From"] = BREVO_SMTP_USER
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp-relay.brevo.com", 587) as server:
            server.starttls()
            server.login(BREVO_SMTP_USER, BREVO_SMTP_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully at {datetime.now()}")
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route("/")
def home():
    return "Flask app is running and scheduler is active!"

# Function to start the scheduler
def start_scheduler():
    scheduler = BackgroundScheduler()
    # Schedule the job to run every weekday at 5:00 AM
    scheduler.add_job(send_email, "cron", day_of_week="mon-fri", hour=15, minute=37)
    scheduler.start()
    print("Scheduler started!")

if __name__ == "__main__":
    start_scheduler()
    app.run(host="0.0.0.0", port=5000)
