import random
zela = random.randint(3,7)

#Isosceles Triangle:
for q in range (zela):
 print (q * " ", end = "")
 print((zela - q) * "* ", end="")
 print("")  


##Isosceles Triangle_ chatgpt:
for q in range(zela):
    for _ in range(q):
        print(" ", end="")
    for _ in range(zela - q):
        print("* ", end="")
    print("")


#Reverse Isosceles Triangle:
for q in range (zela):
 print ((zela - (q + 1)) * " ", end = "")
 print((q + 1) * "* ", end="")
 print("")  

##Reverse Isosceles Triangle_ chatgpt:
for q in range(zela):
    for _ in range(zela - (q + 1)):
        print(" ", end="")
    for _ in range(q + 1):
        print("* ", end="")
    print("")

