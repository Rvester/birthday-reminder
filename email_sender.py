import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv


load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")       
EMAIL_PASS = os.getenv("EMAIL_PASS")       
MAILGUN_SMTP_SERVER = os.getenv("MAILGUN_SMTP_SERVER")
MAILGUN_SMTP_PORT = os.getenv("MAILGUN_SMTP_PORT") 

def send_birthday_email(email, name, coupon):
    
    subject = "Happy Birthday!"
    body = f"Hi {name},\n\nWishing you a wonderful birthday! As a token of our appreciation, here is a special coupon for you: {coupon}\n\nEnjoy!\n\nBest regards,\nYour Team"

   
    msg = EmailMessage()
    msg['From'] = EMAIL_USER
    msg['To'] = email
    msg['Subject'] = subject
    msg.set_content(body)
    
   
    try:
        with smtplib.SMTP(MAILGUN_SMTP_SERVER, MAILGUN_SMTP_PORT) as smtp:
            smtp.starttls() 
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
        print(f"Email sent successfully to {email}")
    except Exception as e:
        print(f"Failed to send email to {email}: {e}")
