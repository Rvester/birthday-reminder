import os
import vonage
from dotenv import load_dotenv

load_dotenv()

def send_birthday_sms(phone_number, name, coupon):
    client = vonage.Client(
        key=os.getenv("VONAGE_API_KEY"), 
        secret=os.getenv("VONAGE_API_SECRET")
    )
    sms = vonage.Sms(client)
    
    message_text = f"Hi {name}! Happy Birthday 🎉! Enjoy a 20% discount with coupon code {coupon}. Have a great day!"

    response = sms.send_message(
        {
            "from": os.getenv("VONAGE_PHONE_NUMBER"),
            "to": phone_number,
            "text": message_text,
        }
    )
    
    if response["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response['messages'][0]['error-text']}")
