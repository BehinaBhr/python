MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

order = "espresso"
def order_needs(order):
    order_ingredients = MENU[order]["ingredients"]
    # order_water = order_ingredients["water"]
    # order_milk = order_ingredients["milk"]
    # order_coffee = order_ingredients["coffee"]
    # return order_water, order_milk, order_coffee
    for item in order_ingredients:
        order_each = order_ingredients[item] 
        print(order_each)


order_needs(order)

    
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

start = True
bank = 0


def calculate(quarter, dime, nickle, penni, order_cost, bank):
    insert_money = (float(quarter) * 0.25) + (float(dime) * 0.10) + (float(nickle) * 0.05) + (float(penni) * 0.01)
    if insert_money >= order_cost:
        change = round(insert_money - order_cost,2)
        print(f"Here is {change} in change.")
        bank += order_cost
        return bank
    else:
        print("Sorry that's not enough money. Money refunded.")

def get_ingredient(order_ingredients, item):
    if item in order_ingredients:
        return order_ingredients[item]
    return 0

def order_needs(order):
    order_ingredients = MENU[order]["ingredients"]
    order_water = get_ingredient(order_ingredients, "water")
    order_milk = get_ingredient(order_ingredients, "milk")
    order_coffee = get_ingredient(order_ingredients, "coffee")
    return order_water, order_milk, order_coffee


def can_order(order):
    order_water, order_milk, order_coffee = order_needs(order)
    if resources["water"] >= order_water and resources["milk"] >= order_milk and resources["coffee"] >= order_coffee:
        able = True
        return able
    else:
        print("Sorry there is not enough resources.")
        able = False
        if resources["water"] < order_water:
            print("Refill the water.")
        if resources["milk"] < order_milk:
            print("Refill the milk.")
        if resources["coffee"] < order_coffee:
            print("Refill the coffee.")
        return able


def make_order(order, able):
    order_water, order_milk, order_coffee = order_needs(order)
    if able:
        print(f"Here is your {order} enjoy!")
    else:
        print("Sorry there is not enough resources.")
        if resources["water"] < order_water:
            print("Refill the water.")
        if resources["milk"] < order_milk:
            print("Refill the milk.")
        if resources["coffee"] < order_coffee:
            print("Refill the coffee.")


def left_resources():
    order_water, order_milk, order_coffee = order_needs(order)
    resources["water"] -= order_water
    resources["milk"] -= order_milk
    resources["coffee"] -= order_coffee


while start:
    print("Hi There, How can I help you?")
    print("1. Order Coffee.")
    print("2. Turn off")
    print("3. Report of resources")
    ask = input("Type the number of one of the above items: ")
    if ask == "1":
        order = input("What would you like? (espresso / latte / cappuccino)  ").lower()
        able = can_order(order)
        if not able:
            continue

        print("Please insert coins.")
        quarter = input("How many quarters? $0.25 *  ")
        dime = input("How many dimes? $0.10 *  ")
        nickle = input("How many nickles? $0.05 *  ")
        penni = input("How many pennies? $0.01 *  ")
        order_cost = MENU[order]["cost"]
        bank = calculate(quarter, dime, nickle, penni, order_cost, bank)
        make_order(order, able)
        left_resources()

    elif ask == "2":
        start = False
        print("Goodbye!")

    elif ask == "3":
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} g")
        print(f"money: $ {bank}")



# TODO: asking "What would you like? (espresso/latte/cappuccino)"
# TODO: asking "Please insert coins.
#   How many quarters? $0.25
#   How many dimes? $0.10
#   How many nickles? $0.05
#   How many pennies? $0.01"
# TODO: For making order:
#      check resources sufficient before order
#      while Recourses At first: Water: 300 ml/ Milk: 200 ml/ Coffe: 100 g/ Money: $0
#      Calculate the money base on cost and available resources:
#      "Sorry that's not enough money. Money refunded."
#      "Sorry there is not enough {sources}"
#        OR: "Here is {} in change."
#            "Here is your {order} enjoy!"

# TODO: able to print report of left resources. Water/ Milk/ Coffe/ Money
# TODO: Turn off the Machine by typing "off"