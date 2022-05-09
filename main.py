import smtplib
import pandas as pd
import datetime as dt
import random

# Crendentials
EMAIL = "wematupythontest2022@gmail.com"
PASSWORD = "Jacques2013"

##################### Extra Hard Starting Project ######################

def birthdays_today():
    try:
        data = pd.read_csv("birthdays.csv")
    except FileNotFoundError:
        print("Birthday data file does not exist")
    else:
        today = dt.datetime.now()
        month = today.month
        day = today.day
        return data[(data["month"] == month) & (data["day"] == day)]

# Send email msg
def send_mail(email_addr, mail_msg):
   try:
        conn = smtplib.SMTP("smtp.gmail.com")
        conn.starttls()
        conn.login(user=EMAIL, password=PASSWORD)
        conn.sendmail(
            to_addrs=email_addr, 
            from_addr=EMAIL,
            msg=f"Subject: Happy Birthday \n\n{mail_msg}")
   except: 
        print("Critical error occured sending mail")
   else:
        print("Email sent")
        conn.close()
        
# Send email to birthday celebrant          
def send_happy_birthday():
    # Get birthdays for today
    birthdays = birthdays_today()
    # Pick letter template , replace and send mail to person
    if len(birthdays):
        for idx, row in birthdays.iterrows():
            try:
                with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as template:
                    template_data = template.read().replace("[NAME]", row["name"])
                    print(template_data)
            except FileNotFoundError:
                print("Birthday template not found")
            else:
               send_mail(email_addr=row["email"], mail_msg=template_data)
    
# Send the letter generated in step 3 to that person's email address. 
send_happy_birthday()





