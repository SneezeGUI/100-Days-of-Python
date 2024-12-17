import smtplib
import datetime as dt
import random

now = dt.datetime.now()

day_of_week = now.weekday()

file_path = 'quotes.txt'

QUOTES = []

smtp_email = 'email'
smtp_password = 'password'

if day_of_week == 0:
    message = random.choice(QUOTES)
    with open(file_path) as quotes:
        for quote in quotes:
            QUOTES.append(quote)
    with smtplib.SMTP(host='SMTP SERVER GOES HERE', port=SMTP_PORT_HERE) as connection:
        connection.starttls()
        connection.login(user=smtp_email, password=smtp_password)
        connection.sendmail(
        from_addr=smtp_email,
        to_addrs= 'RECIPIENT EMAIL GOES HERE',
        msg=f'Subject:Monday Motivation\n\n{message}')
        print('Email Sent.')
else:
    print('Todays not Monday Silly')

