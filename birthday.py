import pandas as pd
import datetime as dt
import random


class BirthdayManager():
    def __init__(self) -> None:
        self.birthdays_today: pd.DataFrame = self.get_birthdays_today()
    
    def get_birthdays_today(self, bd_file = "birthdays.csv") -> pd.DataFrame:
        try:
            data = pd.read_csv(bd_file)
        except FileNotFoundError:
            print("Birthday data file does not exist")
        else:
            today = dt.datetime.now()
            month = today.month
            day = today.day
            return data[(data["month"] == month) & (data["day"] == day)]

      
    def to_send(self) -> list:
        # Pick letter template , replace and send mail to person
        bd_list = []
        for idx, row in self.birthdays_today.iterrows():
                bd_list.append({
                    "email":row["email"], 
                    "msg": self.get_birthday_template(name=row["name"])
                    })
        return bd_list
    
    
    def get_birthday_template (self, name: str, letters_folder = "./letter_templates", letter_start = "letter_", num_of_letters = 3, try_count = 0) -> str:
        try:
            with open(f"{letters_folder}/{letter_start}{random.randint(1, num_of_letters)}.txt") as file:
                        template = file.read()
        except FileNotFoundError as error:
            print(error)
            if try_count == 3:
                print("Could not find ant birthday templates.")
                return "None"
            self.get_birthday_template(try_count= try_count + 1)
        else:
            return template.replace("[NAME]", name) 
            
                