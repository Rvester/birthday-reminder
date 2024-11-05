import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

def send_birthday_email(email, name, coupon):
    yag = yagmail.SMTP(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
    
    subject = f"Happy Birthday, {name}!"
    content = f"""
    Hi {name},

    Wishing you a fantastic birthday! 🎉
    
    Here’s a special gift: use Coupon Code **{coupon}** to enjoy a 20% discount on your next purchase!

    Best wishes,
    Your Friendly Company
    """
    
    yag.send(
        to=email, 
        subject=subject, 
        contents=content
    )
