import csv
from datetime import datetime

def get_today_birthdays(file_path):
    today = datetime.today().strftime('%m-%d')
    birthdays_today = []
    
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['birthday'] == today:
                birthdays_today.append(row)
                
    return birthdays_today
