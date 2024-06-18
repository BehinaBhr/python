#Isosceles Triangle by demand:

def space():
  print(" ", end="")
  
def star():
   print("* ", end="")


while True: 
  user_ask = input ("Please enter 1 for up to down or 2 for reverse: ")
  zela = int(input("Please enter a number for zela: "))

  if user_ask == "1":
    for q in range(zela):
      for _ in range(zela - (q + 1)):
          space()
      for _ in range(q + 1):
          star()
      print("")


  if user_ask == "2":
    for q in range(zela):
      for _ in range(q):
        space()
      for _ in range(zela - q):
        star()
      print("")