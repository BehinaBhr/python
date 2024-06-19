# import smtplib
#
# my_email = "be.bhr77@gmail.com"
# password = "dilz ioyp lyjd hkuk"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="behinabahramsary@yahoo.com",
# msg="Subject:Hi from Python\n\nThis is the body for my email.”)
# connection.close()
# # better way:
# with smtplib.SMTP("smtp.gmail.com") as connection:
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="behinabahramsary@yahoo.com",
# msg="Subject:Hi from Python\n\nThis is the body for my email.”)
# connection.close()

# # # ChatGPT:
# with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="behinabahramsari@gmail.com",
#                         msg="Subject:Hi from Python\n\nThis is the body for my email.")

#
# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
# print(now.year)
# print(now.weekday())
# my_birthday = dt.datetime(year=1998, month=8, day=29, hour=13, minute=40)
# print(my_birthday)

# TODO: send a motivational quote via email on the current day:
#  Use the datetime module to obtain the current day of the week.
#  Open the quotes.txt file and obtain a list of quotes.
#  Use the random module to pick a random quote from your list of quotes.
#  Use the Smtplib to send the email to yourself.



import datetime as dt
import random
import smtplib

my_email = "be.bhr77@gmail.com"
password = "dilz ioyp lyjd hkuk"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as file:
        lines = file.readlines()
        daily_quote = random.choice(lines)

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject: Good Morning from Python\n\n{daily_quote}")
