from birthday import BirthdayManager
from mail import MailManager


# Instances
bd_manager = BirthdayManager()
mail = MailManager()

# check if birthdays today and send wishes
bd_today = bd_manager.to_send()

if len(bd_today): 
    mail.send_birtday_wishes(bd_today)





