#Triangle by demand:


def space():
  print("  ", end="")
  
def star():
   print("* ", end="")

while True: 
  user_ask = input ("Please enter A for left from up to down and C reverse or B for right from up to down and D for reverse: ")
  zela = int(input("Please enter a number for zela: "))
  
  if user_ask == "A":
    for a in range(zela):
      for _ in range(a + 1):
         star()
      print("")
  
  
  if user_ask == "B":
    for b in range(1, zela + 1):
      for _ in range(zela - b):
          space()
      for _ in range(b):
          star()
      print("")
  
  
  if user_ask == "C":
    for c in range(zela):
      for _ in range(zela - c):
          star()
      print("")
  
  
  if user_ask == "D":
   for d in range(zela):
      for _ in range(d):
          print("  ", end="")
      for _ in range(zela - d):
          print("* ", end="")
      print("")  
  