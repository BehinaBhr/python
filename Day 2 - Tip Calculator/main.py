#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# print(round(33.6000,2))
# print("{:.2f}".format(33.6000))

# Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input ("How much is the total bill? $"))
tip = int(input ("What percentage of tip would you like to give? %"))
people = int(input("How many people to split the bill? "))

part = bill * (1 + tip/100) / people
result = round(part,2)
result = "{:.2f}".format(part)
print(f"Each person should pay: ${result}")


