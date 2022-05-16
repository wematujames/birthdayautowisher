import smtplib
import datetime as dt
import os

# Crendentials
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


class MailManager():
    def __init__(self, from_email = EMAIL) -> None:
        self.from_email = from_email
    
    
    def send_birtday_wishes (self, birthdays: list,) -> None:
        for wish in birthdays:
            self.send_mail(email=wish["email"], msg= wish["msg"])
    
    
    def send_mail(self, email: str, msg: str) -> None:
        print(self.from_email, EMAIL, PASSWORD)
        try:
            conn = smtplib.SMTP("smtp.gmail.com")
            conn.starttls()
            conn.login(user=EMAIL, password=PASSWORD)
            conn.sendmail(
                to_addrs=email, 
                from_addr=self.from_email,
                msg=f"Subject: Happy Birthday \n\n{msg}")
        except: 
                print(f"Error sending birthday wish to {email}")
        else:
                print("Email sent")
        finally:
                conn.close()