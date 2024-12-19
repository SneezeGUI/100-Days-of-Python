import random
import smtplib
import datetime as dt
from tkinter import *
from json import *
from tkinter import messagebox
import os

current_time = dt.datetime.now()
last_check = 0
print(current_time)

smtp_email = 'email'
smtp_password = 'password'

data_path = 'birthdays.json'

def day_change_check():
    global last_check
    if last_check == current_time.day:
        print('Checking for date change again in 3 hours...')
        timer = tk.after(3600000,func=day_change_check)
    elif last_check != current_time.day:
        check_and_send()

def check_and_send():
    global last_check
    ##update last checked day
    last_check = current_time.day
    print('Checking for Birthdays')
    try:
        with (open(data_path) as data_file):
            data = load(data_file)
            for name in data:
                name = name
                email = data[name]['email']
                month = data[name]['month']
                day = data[name]['day']

                ##send email if person in people.json has a birthday today
                if current_time.day == int(day) and current_time.month == int(month):
                    #create letter from birthday person name and letter template
                    # create_letter(name)
                    letter_choice = random.randint(1, 3)
                    letter_path = f'letter_templates/letter_{letter_choice}.txt'
                    stripped_name = name.strip()
                    placeholder = "[NAME]"
                    with open(letter_path) as letter:
                        letter_contents = letter.read()
                        new_letter = letter_contents.replace(placeholder, stripped_name)
                    #connect and send email
                    with smtplib.SMTP(host='SMTP SERVER HERE', port=SMTP PORT HERE) as connection:
                        connection.starttls()
                        connection.login(user=smtp_email, password=smtp_password)
                        connection.sendmail(
                            from_addr=smtp_email,
                            to_addrs= email,
                            msg=f'Subject:Happy Birthday!\n\n{new_letter}')
                        print(new_letter)
                        print('Sending Birthday Mail')
            day_change_check()
    except FileNotFoundError:
        os.makedirs('./Output/ReadyToSend/')

def create_letter(name):
    letter_choice = random.randint(1, 3)
    letter_path = f'letter_templates/letter_{letter_choice}.txt'
    stripped_name = name.strip()
    placeholder = "[NAME]"
    with open(letter_path) as letter:
        letter_contents = letter.read()
        new_letter = letter_contents.replace(placeholder, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

# def add_info(name, email, month, day, year): ## USE THIS FUNC NAME IF USING CLI NOT GUI
def add_info():
    name = name_entry.get()
    email = email_entry.get()
    month = birth_month.get()
    day = birth_day.get()
    year = birth_year.get()
    new_data = {
        name: {
            "email": email,
            "month": month,
            "day": day,
            "year": year,
        }
    }
    try:
        with open(data_path) as data_file:
            data = load(data_file)
    except FileNotFoundError:
        with open(data_path, "w") as data_file:
            dump(new_data, data_file, indent=4)

    except JSONDecodeError:
        with open(data_path, "w") as data_file:
            dump(new_data, data_file, indent=4)
    else:
        # Updating old data with new data
        data.update(new_data)

        with open(data_path, "w") as data_file:
            # Saving updated data
            dump(data, data_file, indent=4)
    finally:
        name_entry.delete(0,END)
        email_entry.delete(0, END)
        birth_month.delete(0, END)
        birth_day.delete(0, END)
        birth_year.delete(0, END)

##INPUTS IF USING CLI NOT GUI##
# add_person = input('Would you like to add a Person? (Y/N): ').lower()
# if add_person == 'y':
#     name_entry = input('Name: ')
#     email_entry = input('Email: ')
#     month_entry = input('Birth Month: ')
#     day_entry = input('Birth Day: ')
#     year_entry = input('Birth Year: ')
#     add_info(name=name_entry,email=email_entry,month=month_entry,day=day_entry,year=year_entry)
# else:
#     check_and_send()

##UI##
tk = Tk()
tk.title('Birthday Mailer')
tk.config(padx=20,pady=20)

name_label = Label(text='Name:')
name_label.grid(column=0,row=0)
name_entry = Entry(width=30)
name_entry.grid(column=1,row=0,columnspan=5,)
name_entry.focus()

email_label = Label(text='Email:')
email_label.grid(column=0,row=1)
email_entry = Entry(width=30)
email_entry.grid(column=1,row=1,columnspan=5)

birthday_label = Label(text='Birthday:')
birthday_label.grid(column=0,row=2)

birth_month = Entry(width=8)
birth_month.grid(column=1, row=2)

dash_label = Label(text='-')
dash_label.grid(column=2,row=2)

birth_day = Entry(width=8)
birth_day.grid(column=3,row=2)

dash1_label = Label(text='-')
dash1_label.grid(column=4,row=2)

birth_year = Entry(width=8)
birth_year.grid(column=5,row=2)

add = Button(text='Add Contact Info', command=add_info)
add.grid(column=1,row=3,columnspan=5)

start = Button(text='Start Checking Birthdays', command=check_and_send)
start.grid(column=1,row=4,columnspan=5)

tk.mainloop()




