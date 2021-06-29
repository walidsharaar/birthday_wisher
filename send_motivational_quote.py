import random
import smtplib
import datetime as dt

my_email ="mmytest779@gmail.com"
my_password="1234567@abc%$"

now = dt.datetime.now()
weekday = now.weekday()
# weekday ==0 is monday
if weekday == 1:
    with open("quotes_list.txt") as quotes:
       quotes_list = quotes.readlines()
       quote= random.choice(quotes_list)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:motivation\n\n {quote}")


