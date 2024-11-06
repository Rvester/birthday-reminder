from birthday_checker import get_today_birthdays
from email_sender import send_birthday_email
from sms_sender import send_birthday_sms
from coupon_generator import generate_coupon
import schedule 
import time


file_path = 'birthdays.csv'


today_birthdays = get_today_birthdays(file_path)

for person in today_birthdays:
    name = person['name']
    email = person['email']
    phone_number = person['phone_number']  
    coupon = generate_coupon()
    
   
    
    
    if email:
        send_birthday_email(email, name, coupon)
    
    
    if phone_number:
        send_birthday_sms(phone_number, name, coupon)


# schedule.every().day.at("08:00").do(today_birthdays)

# while True:
#     schedule.run_pending()
#     time.sleep(60)