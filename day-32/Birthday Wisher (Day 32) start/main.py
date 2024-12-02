import smtplib
import random
import datetime as dt



# Open and read a random quote from the file
with open("quotes.txt", "r") as f:
    quotes = f.readlines()
    quote = random.choice(quotes).strip()  # Strip to remove any trailing newline

now = dt.datetime.now()
the_message = f"{quote}\n\n{now.day}/{now.month}/{now.year}, {now.hour}:{now.minute}"
print(the_message)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="apawlos0@gmail.com",
        msg=f"Subject: Daily Quote\n\n{the_message}"  # Use `the_message` here
    )
