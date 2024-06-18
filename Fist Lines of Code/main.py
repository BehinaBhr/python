#Sring:
print("Hello Behina, It's your first experience.")

#Integer:
day = 22
print(day)
temp = -10
print(temp)

#Float:
weight = 136.25
print(weight)
score = -2.5
print(score)

#Math:
print(-3 + 6)
print(weight / 2)
print(score * 2)
print(weight + score)

#Variable in string:
movie = '"love"and other drugs'
print(movie)
challange = "the king's\"speech\"" 
print(challange)
anotherchallange = 'the king\'s"speech"'
print(anotherchallange)

date = 22 
day_name = "Monday"
month = "Jun"
degree = 16
print(f"Today is {day_name} {month} {date} and It's {degree} centigrade outside")

#Boolean:
weather_is_cold = True
if weather_is_cold:
  print("It's cold")
  print("Be careful!")
else:
  print("enjoy it!")

#If, else, comparisons:
age = 22
if age >= 18:
  # print(age >= 18) --> True
  print(f"{age},You're an adult")
else:
  print(f"{age},You're an child")

#Random:
#dice:
import random
print(random.randint(1,6))
print(random.random())
#magic_8_ball:
answers = random.randint(1,3)
if answers == 1:
  print("yes")
if answers == 2:
  print("maybe")
if answers == 3:
  print("No")

#fortune_cookie:
lucky_number = random.randint(1,100)
fortune_number = random.randint(1,3)
fortune_text = ""
if fortune_number == 1:
  fortune_text = "You will have a great day."
if fortune_number == 2:
  fortune_text = "You can change anything to what you want."
if fortune_number == 3:
  fortune_text = "Today will be tough, but worth it."

print (f"{fortune_text} Your lucky number is {lucky_number}")

#Lists:
fav_list = [1,5.6,"Sandlot"]
print(fav_list[0])

fav_number = [3,7,77,48,1998]
print(len(fav_number))

fav_movies = ["sandlot", "The Lego Movie", "Dune"]
print(len(fav_movies))
print(fav_movies)

fav_movies.append("iron Man")
print(len(fav_movies))
print(fav_movies)

fav_movies.insert(1,"Batman")
print(fav_movies)

del(fav_movies[2])
print(fav_movies)

del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[0])
print(fav_movies)

# For-loop and list:
for number in range(5):
 print("Hello")
 print ("Hi there")
 
for x in range(5):
 print(x)

fav_films = ["Sandlot", "The Lego Movie", "Dune"] 
for film in fav_films:
 print(film)

for y in range(10):
 print((y+1)*2)

# Dictionary: 
cats = {"Jane":6, "Tom":14, "Sara":8}
print(cats)
print(cats["Tom"])

cats["wilson"] = 1
print(cats)

del(cats["Tom"])
print(cats)

len(cats)
print(len(cats))

#another example:
odd_nums = {0:False, 1:True, 2:False, 3:True, 4:False, 5:True}
print(odd_nums)

print(odd_nums[4])

odd_nums[6] = False
odd_nums[7] = True
print(odd_nums)

del(odd_nums[0])
print(odd_nums)

print(len(odd_nums))

#Splitting a string:
ugly_text = "The club isn't the best place to find a lover So the bar is where I go Me and my friends at the table doing shots Drinking fast and then we talk slowCome over and start up a conversation with just me And trust me I'll give it a chance now Take my hand, stop, put Van the Man on the jukebox And then we start to dance, and now I'm singing like"
print(ugly_text)

text = """The club isn't the best place to find a lover
So the bar is where I go
Me and my friends at the table doing shots
Drinking fast and then we talk slow
Come over and start up a conversation with just me
And trust me I'll give it a chance now
Take my hand, stop, put Van the Man on the jukebox
And then we start to dance, and now I'm singing like
Girl, you know I want your love
Your love was handmade for somebody like me
Come on now, follow my lead
I may be crazy, don't mind me
Say, boy, let's not talk too much
Grab on my waist and put that body on me
Come on now, follow my lead
Come, come on now, follow my lead
I'm in love with the shape of you
We push and pull like a magnet do
Although my heart is falling too
I'm in love with your body
Last night you were in my room
And now my bedsheets smell like you
Every day discovering something brand new
I'm in love with your body
(Oh-I-oh-I-oh-I-oh-I)
I'm in love with your body
(Oh-I-oh-I-oh-I-oh-I)
I'm in love with your body
(Oh-I-oh-I-oh-I-oh-I)
I'm in love with your body
Every day discovering something brand new
I'm in love with the shape of you"""
print(text)
print(len(text))
print(text.split())
print(len(text.split()))

#Counting the words:
essay = """a b c a a b"""
print(essay.split())
word_count = {}
for word in essay.split():
   print(word)
  
 # word_count[word] = 1
 # print(word_count)
  
   if word in word_count:
     word_count[word] += 1
   else:
     word_count[word] = 1
print(word_count)

#lowercase:
content = """a b c a A b A C"""
print(content.lower().split())
for word in content.lower().split():
   print(word)
   if word in word_count:
     word_count[word] += 1
   else:
     word_count[word] = 1
print(word_count)

#longertext:
print(text.lower().split())
for word in text.lower().split():
   # print(word)
   if word in word_count:
     word_count[word] += 1
   else:
     word_count[word] = 1
print(word_count)

#Function:
def bark():
   print("Hup Hup!")
   print("Hi,I'm a dog!")
bark()
bark()

for x in range(3):
   bark()

def hello():
   print("Hello there! How are you today?")
hello()

#Parameter:
def hello(name):
   print(f"Hello {name}! How are you today?")
hello("Sara")

def add_number(num1, num2):
   print(f"{num1} + {num2} =")
   print(num1 + num2) 
add_number(4,8)
add_number(3,7)

def dog_info(name,age):
    print(f"Hi! I'm {name} and {age} years old.")
dog_info("Fido",8)
dog_info("Sara",4)

#Returning:
def double(number):
   print(number * 2) 
double(5)

new_number = double(7)
print(new_number)

def triple(number):
  return number * 3
print(triple(6))

new_number = triple(7)
print(new_number)

def caps(letter):
  return letter.upper()
print(caps("you are here with me."))

people = ["nick", "sara", "jane"]
for name in people:
  print(caps(name))

#Comment: 
#I'm sad for losing the whole notes:((

#Input:
user_text = input("Please enter some Text: ")
print(user_text)
print(user_text.upper())
print(user_text.lower())

user_demand = input("Please enter sth to be doubled: ")
print(user_demand * 2)

user_number = input("Please enter number to be doubled: ")
print(int(user_number) * 2)

user_typing = input("Please type sth: ")
user_ask = input ("Please enter 1 to uppercase or 2 for lowercase: ")
if user_ask == "1":
   print(user_typing.upper())
else:
   print(user_typing.lower())
  
#Gameloop_Numberguesser:
import random
import time
print("Hi, Welcome! Please guess a number between 1 and 100")
time.sleep(2)
guess = int(input("What is your guess?"))
correct_number = random.randint(1,100)
count = 1
while guess != correct_number:
  count += 1
  print("False!")
  time.sleep(1)
  if guess < correct_number:
      guess = int(input("Guess higher. Next guess? "))
  else:
     guess = int(input("Guess lower. Next guess? "))
  
print(f"True! {correct_number} is correct answer. It took you {count} guesses.")

