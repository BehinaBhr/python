print ("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("Ok! You can ride.")
  age = int(input("How old are you? "))
  if age < 12:
    print("You need Cild tickets.")
    bill = 5
  elif age <= 18:
    print("You need Youth tickets.")
    bill = 7
  elif age >= 44 or age <= 55:
    print("You get a free ticket.")
    bill = 0
  else:
    print ("You need Adault ticket.")
    bill = 12
  print(f"Your ticket is ${bill}")
    
  photo = input("Do you wan a photo taken? Yes or No\n")
  if photo == "Yes":
      bill += 3
  print(f"Here you are! Total is ${bill}")
    
  
else:
  print("Sorry! You can not ride.")