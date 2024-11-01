import yagmail
from dotenv import load_dotenv
import os
from coupon_generator import generate_coupon

load_dotenv()
SENDER_EMAIL = os.getenv("EMAIL_USER")
SENDER_PASSWORD = os.getenv("EMAIL_PASS")

def send_birthday_email(email, name):
    yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
    coupon = generate_coupon()
   
    subject = f"Happy Birthday!"
    content = f"Dear {name},\n\nHappy birthday!🎂🎇❤️ We hope you have a great day. As a gift, we're offering you a special discount code: {coupon}.\n\nBest regards,\nYour team"

    yag.send(to=email, subject= subject, contents = content)
    print(f"Email sent to {name} at {email} succesfully!")
    