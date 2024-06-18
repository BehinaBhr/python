#Areas:
def area_triangle (base, height):
    return base*height /2

area_a = area_triangle (5,4)
area_b = area_triangle (7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str (sum))



#How many hours,minutes,seconds are in a given amount of seconds:
def convert(sec):
    h = sec // 3660
    min = (sec % 3600) // 60
    remain = sec - (h*3600 + min *60)
    return h, min, remain
h,min,remain = convert(15000)
# print(h,min)
print(f"is equal to {h} hours and {min} minutes and {remain} seconds ")

#lucky numbers:
name = "Kay"
number = len (name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))
name = "Cameron"
number = len (name) * 9
print("Hello " + name + ". Your lucky number is " + str (number))

#clean
def number(name):
   return len(name) * 9

name = "Behina"
print(f"Hello {name} Your lucky number is {number(name)}")

#clean
def number(name):
    return len(name) * 9
    
result = number("Behina")
print(f"Hello {name} Your lucky number is {result}")


#clean_withoutreturn
def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number ("Kay")



#How many days are in a variable number of years, months, and days?
#clean
def day_convert(year, month, day):
    return (year * 365) + (month * 30) + day
  
the_day = day_convert(2,5,23)
print(f"total days are {the_day}")


#clean_withoutreturn
def day_convert(year, month, day):
    the_day = (year * 365) + (month * 30) + day
    print(f"total days are {the_day}")
  
day_convert(2,5,23)



#fluid ounces to milliliters
#clear_withoutreturn
def volume_convert(oz):
    ml = oz * 29.5735
    print("= ", str(ml))

volume_convert(2)


#clean
def volume_convert(oz):
    return oz * 29.5735

ml = volume_convert(2)
print("= ", str(ml), f"which is approximatly {int(ml)} ml" )


#clean
def volume_convert(oz):
    return oz * 29.5735

oz = 2
print("= ", volume_convert(oz), f"which is approximatly {int(volume_convert(oz))} ml" )


#clean
def volume_convert(oz):
    ml = oz * 29.5735
    return ml

oz = 2
print("= ", str(ml), f"which is approximatly {int(ml)} ml" )


# make an increasing order:
#1
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1


smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

#2
def order(num1, num2):
	if num1 > num2:
		return num2, num1
	else:
		return num1, num2

smaller, bigger = order_numbers(200, 99)
print(smaller, bigger)