from twilio.rest import Client
from dotenv import load_dotenv
import os
from coupon_generator import generate_coupon

load_dotenv()
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")

def send_birthday_sms(phone, name):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    coupon = generate_coupon()
    
    message = client.messages.create(
        body=f"Dear {name},\nHappy birthday!🎂🎇❤️ We hope you have a great day. As a gift, we're offering you a special discount code: {coupon}.\nBest regards,\nYour team",
        from_=TWILIO_PHONE,
        to=phone
    )
    
    print(f"SMS sent to {name} at {phone} succesfully!")