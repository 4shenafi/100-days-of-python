import pandas as pd
import datetime as dt
import smtplib
import random

my_email = 'chalakumsa@gmail.com'
password = '123456789'

birthday_file = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
today_month = now.month
today_day = now.day

birthdays_dict = {(row['month'], row['day']): row for _, row in birthday_file.iterrows()}

if (today_month, today_day) in birthdays_dict:
    birthday_person = birthdays_dict[(today_month, today_day)]
    recipient_name = birthday_person['Name']
    recipient_email = birthday_person['Email']

    letter_template_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(letter_template_path, 'r') as letter_template:
        letter_content = letter_template.read()
        final_letter_content = letter_content.replace("[NAME]", recipient_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:Happy Birthday!\n\n{final_letter_content}"
        )
