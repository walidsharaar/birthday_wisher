import datetime as dt
# 1.Check if today matches a birthday in the birthdays.csv
# 2.Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
import smtplib
import pandas
import random

my_email ="mmytest779@gmail.com"
my_password="1234567@abc%$"

today = (dt.datetime.now().month,dt.datetime.now().day)
# 3. Use pandas to read the birthdays.csv
# Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
data=pandas.read_csv("birthdays.csv")
#4.Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# test,test@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): test,test@email.com,1995,12,24
# }
birthdays_dict = {(data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()}
#5.Compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
#5.If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter.
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path= f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content= letter_file.read()
        contents=content.replace("[NAME]",birthday_person["name"])
# 6. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(my_email,my_password)
        conn.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],
                      msg=f"Subject: Happy Birthday!\n\n{contents}")


