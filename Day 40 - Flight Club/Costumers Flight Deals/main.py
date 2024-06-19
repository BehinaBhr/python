import sheety

print("Welcome to Behi's Flight Club.\n We find the best flight deals and email you.")
name = input("What is your First name?\n").title()
last_name = input("What is your Last name?\n").title()
email = input("What is your email address?\n")
dub_email = input("Type your emai address agsin to confirm.\n ")
if email == dub_email:
    print("Thank you for choosing us, You're in the club.")


sheety.post_new_row(name, last_name, email)