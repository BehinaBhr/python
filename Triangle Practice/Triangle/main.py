import random
zela = random.randint(4,7)

#Triangle A:
for a in range(zela):
  print((a + 1) * "* ")

#Revers Triangle B:
for b in range(1, zela + 1):
  print((zela - b) * "  ", end="")
  print(b * "* ", end=" ")
  print("")  

#Revers Triangle C:
for c in range(zela):
  print((zela - c) * "* ", end="")
  print("") 

#Revers Triangle D:
for d in range (zela):
 print (d * "  ", end="")
 print((zela - d) * "* ", end="")
 print("")  



##Triangle A _ chatgpt:
for a in range(zela):
    for _ in range(a + 1):
        print("* ", end="")
    print("")
  
##Triangle B _ chatgpt:
for b in range(1, zela + 1):
    for _ in range(zela - b):
        print("  ", end="")
    for _ in range(b):
        print("* ", end="")
    print("")
  
##Triangle C_ chatgpt:
for c in range(zela):
    for _ in range(zela - c):
        print("* ", end="")
    print("")
  
##Triangle D_ chatgpt:
for d in range(zela):
    for _ in range(d):
        print("  ", end="")
    for _ in range(zela - d):
        print("* ", end="")
    print("")  



