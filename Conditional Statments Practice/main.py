#count the figure of salary:
def figure(salary):
  count = 0
  if salary == 0:
        count += 1
  while salary >= 1:
    salary = salary/10
    count += 1
    
  return count

print("It is " + str(figure(230000000)) + "-figure salary.")
 
  



#elevator_1:

def elevator_floor(enter, exit):
  floor = enter
  elevator_direction = ""
  if exit < enter:
        elevator_direction = "Going down: "
        while exit <= floor:
            elevator_direction += str(floor) + " | "
            floor -= 1

  else:
        elevator_direction = "Going up: "
  
        while exit >= floor:
            elevator_direction += str(floor) + " | "
            floor += 1

  return elevator_direction.strip(" | ")


 
print(elevator_floor(1,4)) 
print(elevator_floor(6,2)) 


#elevator_2:
def elevator_floor(enter, exit):
    elevator_direction = "Going "
    
    if exit < enter:
        elevator_direction += "down: "
        for floor in range(enter, exit - 1, -1):
            elevator_direction += str(floor) + " | "
    else:
        elevator_direction += "up: "
        for floor in range(enter, exit + 1):
            elevator_direction += str(floor) + " | "

    return elevator_direction.strip(" | ")
  
print(elevator_floor(8,5))
print(elevator_floor(5,8))

#count_factor:
def count_factors(number):
  factor = 1
  count = 0
  result = f"factors for {number}: "
  
  if number == 0:
    return result + "0"
 

  while factor < number and number // factor >= factor:
   
    if number % factor == 0:
      count += 2
      result += "(" + str(factor) + " x " + str(number // factor)  + ") "   
      
      
    factor += 1
 
  return str(count) + " " + result 
  

print(count_factors(0)) # Count value will be 0
print(count_factors(3)) # Should count 2 factors (1x3)
print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8,
# and 4x6). 
print(count_factors(84)) # Should count 12 factors (1 x 84) (2 x 42) (3 x 28) (4 x 21) (6 x 14) (7 x 12). 




# 5 lines of the addition table until the sum is lees than 20:
def addition_table(number):
  add = 1
  sum = 1
  result = f"addition_table of {number}: "
  
  while add <= 5:
    sum = number + add
    
    if sum >= 20: 
        result += "None"
        break
        
      
    result += "[" + str(number) + " + " + str(add) + " = " + str(sum) + "] "  
    add += 1
    
  return result

print(addition_table(5))
print(addition_table(17))
print(addition_table(40))


#lines of the multiple table until the result is lees than 50:
multiplier = 1
result = multiplier*5
while result <= 50:
  print(result)
  multiplier += 1
  result = multiplier*5
print("Done")


#lines of the multiple table until the result is lees than 50:
multiplier = 1
result = 5
while result <= 50:
    print(f"{multiplier} x 5 = {result}")
    multiplier += 1
    result = multiplier * 5

print("Done")


#factorial:
def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n -= 1 # Decrement the appropriate variable by -1
    return result


print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1

for sum in range (5):
  sum+=sum
  print(sum)




#Q
num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)