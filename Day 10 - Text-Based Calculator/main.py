from replit import clear
from art import logo

# ###### Way1:
# def calculate(f_num, s_num, op):
#     if op == "+":
#         result = float(f_num) + float(s_num)    
#     elif op == "-":
#         result = float(f_num) - float(s_num)
#     elif op == "*":
#         result = float(f_num) * float(s_num)
#     elif op == "/":
#         result = float(f_num) / float(s_num)
#     print(f"{f_num} {op} {s_num} = {result}")
#     return result

# first_try = True
# while first_try:
#     print(logo)
#     f_num = input("What is the first number? ")
#     print(" +\n -\n *\n /")
#     op = input("Pick an operation. ")
#     s_num = input("What is the second number? ")
#     answer = calculate(f_num, s_num, op) 
#     play = input(f"Type 'y' to continue calculating with {answer} or Type 'n' to start a new one. ").lower()
    
#     while play == "y":
#         f_num = answer
#         s_num = input("What is the next number? ")
#         op = input("Pick an operation. ")
#         answer = calculate(f_num, s_num, op)
#         play = input(f"Type 'y' to continue calculating with {answer} or Type 'n' to start a new one. ").lower()
#     if play == "n":
#         clear()    





###### Way2:
start = True
while start:
    print(logo)
    f_num = input("What is the first number? ")
    print(" +\n -\n *\n /")
    op = input("Pick an operation. ")
    s_num = input("What is the second number? ")
   
    def calculate():
        if op == "+":
            result = float(f_num) + float(s_num)    
        elif op == "-":
            result = float(f_num) - float(s_num)
        elif op == "*":
            result = float(f_num) * float(s_num)
        elif op == "/":
            result = float(f_num) / float(s_num)
        print(f"{f_num} {op} {s_num} = {result}")
        return result
        
    answer = calculate() 
    
    play = input(f"Type 'y' to continue calculating with {answer} or Type 'n' to start a new one. ").lower()

    while play == "y":
        f_num = answer
        s_num = input("What is the next number? ")
        op = input("Pick an operation. ")
        answer = calculate()
        play = input(f"Type 'y' to continue calculating with {answer} or Type 'n' to start a new one. ").lower()
        
    if play == "n":
        clear()


#### Video Solution
from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()

    
    
