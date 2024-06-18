#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised: e.g. 4 letter, 2 symbol, 2 number = JduE&!91

## Way 1
# password = ""
## for l in range(nr_letters) = for l in range(1, nr_letters + 1)
# for l in range(nr_letters): 
#   index_letters = random.randint(0,len(letters)-1)
#   password += str(letters[index_letters])
# for s in range(nr_symbols):
#   index_symbols = random.randint(0,len(symbols)-1)
#   password += str(symbols[index_symbols])
# for n in range(nr_numbers):
#   index_numbers = random.randint(0,len(numbers)-1)
#   password += str(numbers[index_numbers])
# print(password)

## Way 2:
password = ""
for l in range(nr_letters):
  password += random.choice(letters) 
for s in range(nr_symbols):
  password += random.choice(symbols)
for n in range(nr_numbers):
  password += random.choice(numbers)
print(password)

#Hard Level - Order of characters randomised: e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Way 1:
list_index_password = []
rand_result = ""
while len(rand_result) < len(password):
  index_password = random.randint(0, len(password)-1)
  if index_password in list_index_password:
    continue
  list_index_password.append(index_password)
  rand_result += password[index_password]
print(rand_result)


## Way 2:
# list_index_password = []
# rand_result = ""
# while len(list_index_password) < len(password):
#     index_password = random.randint(0, len(password) - 1)
#     if index_password not in list_index_password:
#         list_index_password.append(index_password)
#         rand_result += password[index_password]
# print(rand_result)



## Way 3:
# list_password = list(password)
# list_index_password = []
# rand_result = ""
# while len(list_index_password) < len(list_password):
## index_password = random.randint(0, len(list_password)-1) = random.choice(list_password) 
#   index_password = random.choice(list_password) 
#   if index_password not in list_index_password:
#     list_index_password.append(index_password)
#     rand_result += str(list_password[index_password]) 
# print(rand_result)



## Way 1 with shuffle:
# list_password = list(password)
# rand_result = ""
# random.shuffle(list_password)
# # rand_list_password = random.shuffle(list_password)
# for p in list_password:
#   rand_result += p
# print(rand_result)


## Way 2 with shuffle and join:
# list_password = list(password)
# rand_result = ""
# random.shuffle(list_password)
# print(list_password)
# rand_result = ''.join(list_password)
# # rand_list_password = random.shuffle(list_password)
# # rand_result = ''.join(rand_list_password)
# print(rand_result)




##delete the selected one from list:

## Way 1:
# list_password = list(password)
# rand_result = ""
# for p in range(len(list_password)):
#     index_password = random.randint(0, len(list_password) - 1)
#     rand_result += list_password[index_password]
#     list_password = list_password[:index_password] + list_password[index_password + 1:]
# print(rand_result)


## Way 2 with pop:
# list_password = list(password)
# rand_result = ""
# for p in range(len(list_password)):
#     index_password = random.randint(0, len(list_password) - 1)
#     rand_result += str(list_password.pop(index_password))
# print(rand_result)


## Way 3 with del:
# list_password = list(password)
# rand_result = ""
# while list_password:
#     index_password = random.choice(range(len(list_password)))
#     rand_result += list_password[index_password]
#     del list_password[index_password]
# print(rand_result)