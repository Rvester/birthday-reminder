import pandas as pd
from datetime import datetime


def get_today_birthdays(file_path):
    birthdays = pd.read_csv(file_path)
    today = datetime.today().strftime('%m-%d-%Y')
    birthdays['birthday'] = pd.to_datetime(birthdays['birthday']).dt.strftime('%m-%d-%Y')

    return birthdays[birthdays['birthday'] == today]