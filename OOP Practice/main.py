# defining Classe and object
print("# defining Classe and object")
class Person:
  hair = ""
  eye = ""
  skin = ""

behina = Person()
behina.hair = "brown"
behina.eye = "brown"
behina.skin = "white"

print(behina.hair.upper())
print(behina.eye.upper())
print(behina.skin.upper())

print(' ')
# constructor and special method 
print("# constructor and special method")

class Person:
  def __init__(self,name, hair, eye, skin):
    self.name = name
    self.hair = hair
    self.eye = eye
    self.skin = skin
  
  def __str__(self):
    return "This person is {} with {} hairs and {} eyes and {} skin".format(self.name, self.hair, self.eye, self.skin)
    
behina = Person("Behina", "brown", "brown", "white")  
print(behina)

# ?
print("???????????????????????")
class Person:
  def __init__(self, name, hair, eye, skin):
    self.name = name
    self.hair = hair
    self.eye = eye
    self.skin = skin

  def describe_person(self):
    return "This person is {} with {} hairs and {} eyes and {} skin".format(self.name, self.hair, self.eye, self.skin)

behina = Person("Behina", "brown", "brown", "white")
print(behina.describe_person())
# print(describe_person(behina))?


print(' ')
# challenge 1:
print("# challenge 1:")

class Furniture:
  color = ""
  material = ""
  kind = ""

table = Furniture()
table.color = "brown"
table.material = "wood"
table.kind = "table"

couch = Furniture()
couch.color = "red"
couch.material = "leather"
couch.kind = "couch"

def describe_furniture(piece):
	return ("This {} of furniture is made of {} {}".format(piece.kind, piece.color, piece.material))
  
print(describe_furniture(table)) 
# Should be "This table of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This couch of furniture is made of red leather"


# my change
print("# my change")
class Furniture:
  color = ""
  material = ""
  kind = ""
  
  def __str__(piece):
	   return ("This {} of furniture is made of {} {}".format(piece.kind, piece.color, piece.material))
    
table = Furniture()
table.color = "brown"
table.material = "wood"
table.kind = "table"

couch = Furniture()
couch.color = "red"
couch.material = "leather"
couch.kind = "couch"

print(table) 
print(couch) 



# better 
print("# better ")

class Furniture:
  def __init__(self,color, material, kind):
    self.color = color
    self.material = material
    self.kind = kind
  
  def __str__(piece):
	   return ("This {} of furniture is made of {} {}".format(piece.kind, piece.color, piece.material))
    
table = Furniture("brown", "wood", "table")
couch = Furniture("red","leather", "couch")
print(table) 
print(couch) 


# or
print("# or")

class Furniture:
  def __init__(self,color, material, kind):
    self.color = color
    self.material = material
    self.kind = kind
    
  def describe_furniture(piece):
	   return ("This {} of furniture is made of {} {}".format(piece.kind, piece.color, piece.material))

table = Furniture("brown", "wood", "table")
couch = Furniture("red","leather", "couch")

print(describe_furniture(table)) 
print(describe_furniture(couch)) 



print(' ')
# challenge 2:
print("# challenge 2:")

class City:
    name = ""
    country = ""
    elevation = 0
    population = 0


city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052


city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675


city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
  
    return_city = City()

    if city1.population >= min_population and city1.elevation > return_city.elevation:
        return_city = city1

   
    if city2.population >= min_population and city2.elevation > return_city.elevation:
        return_city = city2

    if city3.population >= min_population and city3.elevation > return_city.elevation:
        return_city = city3

    # Format the return string
    if return_city.name:
        return "{}, {}".format(return_city.name, return_city.country)
    else:
        return ""

print(max_elevation_city(100000))   # Should print "Cusco, Peru"
print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""


print(' ')
# Challenge 3:
print("# Challenge 3:")

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    ex = you.apples
    you.apples = me.apples
    me.apples = ex
    return you.apples, me.apples

def exchange_ideas(you, me):
  
    total_ideas = you.ideas + me.ideas
    you.ideas = total_ideas
    me.ideas = total_ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


print(' ')
# challenge 4:
print("# challenge 4:")

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(p1, p2):
    return p1.apples, p2.apples

def exchange_ideas(p1, p2):
  
    total_ideas = p1.ideas + p2.ideas
    p1.ideas = total_ideas
    p2.ideas = total_ideas
    return p1.ideas, p2.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(martin.apples, johanna.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


print(' ')
# challenge 5:
print("# challenge 5:")

class Piglet:
  def voice(self):
    print("oink oink")
          
hamlet = Piglet()
hamlet.voice()

#step 1
class Piglet:
  name = "no name piglett"
  def speak(self):
      print("Oink! I'm {}! Oink!".format(self.name))

#default name = no name piglett
unknown = Piglet()
unknown.speak()

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

#step 2
class Piglet:
  year = 0
  def age(self):
    return self.year * 18

#default year = 0
unknown = Piglet()
print(unknown.age())

piggy = Piglet()
piggy.year = 2
print(piggy.age())




print("--------------------------------------------------------------------------------------------") 

# inheritance 
print("# inheritance")

class Animal:
  def __init__(self, name, sound):
    self.name = name
    self.sound = sound
  def speak(self):
    print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Piglet(Animal):
   pass
class Cow(Animal):
  pass
  
hamlet = Piglet("HAMLET", "Oink")
milky = Cow("MILKY","Moooo") 
hamlet.speak()
milky.speak()

print(' ')
# challenge 1:
print("# challenge 1:")

# way 1:
class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material = "Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

# way 2:
class Clothing:
  def __init__(self,name,material):
    self.name = name
    self.material = material
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  pass
  
polo = Shirt("Polo", "cotton")
polo.checkmaterial()

print(" ")
# composition
print("# composition")
# You can have a situation where two different classes are related, but there is no inheritance going on. This is referred to as composition --where one class makes use of code contained in another class. For example, imagine we have a Package class which represents a software package. It contains attributes about the software package, like name, version, and size. We also have a Repository class which represents all the packages available for installation. While there’s no inheritance relationship between the two classes, they are related. The Repository class will contain a dictionary or list of Packages that are contained in the repository.
class Package:
  def __init__(self, name, version, size):
    self.name = name
    self.version = version
    self.size = size

class Repository:
  def __init__(self):
    self.packages = {}
  def add_package(self, package):
    self.packages[package.name] = package
  def total_size(self):
    result = 0
    for package in self.packages.values():
      result += package.size
    return result


# Create Package instances
package1 = Package("MyApp", "1.0", 50)
package2 = Package("AnotherApp", "2.5", 80)

# Create a Repository instance
repository = Repository()

# Add packages to the repository
repository.add_package(package1)
repository.add_package(package2)

# Calculate the total size of packages in the repository
total_package_size = repository.total_size()
print("Total package size in the repository:", total_package_size)



print(' ')
# challenge 2:
print("# challenge 2:")

# Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. When you’re finished, the script should add up to 10 cotton clothing items.
# way Q
class Clothing:
  stock = {'name': [],'material' :[], 'amount':[]}
  material = ""
  
  def __init__(self, name):
    self.name = name
    
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
    
  def Stock_by_Material(self, material):
    count = 0
    n = 0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
    n+=1
    return count

class shirt(Clothing):
  material="Cotton"
  
class pants(Clothing):
  material="Jean"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)

# way 2
class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}
    material = ""
    def __init__(self, name, material=""):
        self.name = name
        self.material = material

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(name)
        Clothing.stock['material'].append(material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for n, element in enumerate(Clothing.stock['material']):
            if element == material:
                count += Clothing.stock['amount'][n]
        return count

class Shirt(Clothing):
  material = "Cotton"
  
class Pants(Clothing):
  material = "Jean"

polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)



# Sadjad
class Clothing:
  stock = {}
  material = ""

  def __init__(self, name):
    self.name = name
    
  def add_item(self, amount):
    if self.material not in Clothing.stock:
      Clothing.stock[self.material] = 0
    Clothing.stock[self.material] += amount
    
  def Stock_by_Material(self, material):
      return Clothing.stock[material]

class Shirt(Clothing):
  material = "Cotton"
  
class Shorts(Clothing):
  material = "Lee"
  
polo = Shirt("Polo")
sweatpants = Shorts("Sweatpants")
polo.add_item(4)
sweatpants.add_item(6)
# print(Clothing.stock)
# print(polo.stock)
# print(sweatpants.stock)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


print(' ')
# challenge 3:
print("# challenge 3:")

class Animal:
    def __init__(self, name):
        self.name = name
        self.category = ""  

    def set_category(self, category):
        self.category = category 

class Turtle(Animal):
    def __init__(self, name):
        super().__init__(name)  
        self.category = "reptile"  

class Snake(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.category = "reptile"

class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal  

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal.category == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle")  
snake = Snake("Snake")  
zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile"))  


print(' ')
# challenge 4:
print("# challenge 4:")

import random

class Server:
    def __init__(self):
        self.connections = {}

    def add_connection(self, connection_id):
        connection_load = random.random() * 10 + 1
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        if connection_id in self.connections:
            del self.connections[connection_id]

    def load(self):
        total = sum(self.connections.values())
        return total

    def __str__(self):
        return "{:.2f}%".format(self.load())


server = Server()
server.add_connection("192.168.1.1")
print(server.load())

server.close_connection("192.168.1.1")
print(server.load())

class LoadBalancing:
    def __init__(self):
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        server = random.choice(self.servers)
        self.connections[connection_id] = server
        server.add_connection(connection_id)

    def close_connection(self, connection_id):
        if connection_id in self.connections:
            server = self.connections[connection_id]
            server.close_connection(connection_id)
            del self.connections[connection_id]

    def avg_load(self):
        total_load = sum(server.load() for server in self.servers)
        avg_load = total_load / len(self.servers)
        return avg_load

    def ensure_availability(self):
        if self.avg_load() > 50:
            new_server = Server()
            self.servers.append(new_server)

    def __str__(self):
        loads = [str(server) for server in self.servers]
        return "[" + ",".join(loads) + "]"


l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())



print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# Imagine we have a coffee shop with a bunch of coffee machines (servers), and customers (connections) who come in to order coffee. Each customer places an order that corresponds to a certain amount of coffee (load) they want. The CoffeeMachines represent the coffee machines in the shop that handle the orders.The CoffeeShop manages the orders and CoffeeMachines, ensuring that the average coffee load stays reasonable by adding new machines if needed.

import random

class CoffeeMachine:
    def __init__(self):
        self.orders = {}

    def take_order(self, customer_name):
        coffee_amount = random.random() * 10 + 1
        self.orders[customer_name] = coffee_amount

    def serve_order(self, customer_name):
        if customer_name in self.orders:
            del self.orders[customer_name]

    def coffee_load(self):
        total_coffee = sum(self.orders.values())
        return total_coffee

    def __str__(self):
        return "{:.2f} cups".format(self.coffee_load())

class CoffeeShop:
    def __init__(self):
        self.orders = {}
        self.machines = [CoffeeMachine()]

    def place_order(self, customer_name):
        machine = random.choice(self.machines)
        self.orders[customer_name] = machine
        machine.take_order(customer_name)
        self.ensure_capacity()

    def serve_order(self, customer_name):
        if customer_name in self.orders:
            machine = self.orders[customer_name]
            machine.serve_order(customer_name)
            del self.orders[customer_name]

    def avg_coffee_load(self):
        total_coffee = sum(machine.coffee_load() for machine in self.machines)
        avg_coffee = total_coffee / len(self.machines)
        return avg_coffee

    def ensure_capacity(self):
        if self.avg_coffee_load() > 5:
            new_machine = CoffeeMachine()
            self.machines.append(new_machine)

    def __str__(self):
        loads = [str(machine) for machine in self.machines]
        return "[" + ",".join(loads) + "]"


coffee_shop = CoffeeShop()

coffee_shop.place_order("Alice")
print(coffee_shop.avg_coffee_load())

coffee_shop.machines.append(CoffeeMachine())
print(coffee_shop.avg_coffee_load())

coffee_shop.serve_order("Alice")
print(coffee_shop.avg_coffee_load())

for customer in range(20):
    coffee_shop.place_order("Customer" + str(customer))
print(coffee_shop)

print(coffee_shop.avg_coffee_load())


print(' ')
# challenge 5:
print("# challenge 5:")

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key = get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
#line below is newly added
          if event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)
    return machines


#The error message is likely due to the attempt to remove a user from a machine they were not logged into, specifically during the "logout" event. To fix this issue, you can modify the `current_users` function to only remove a user from a machine if they were previously logged in to that machine. You can achieve this by checking if the user exists in the set of users for that machine before attempting to remove them.Here's the modified version of the `current_users` function:
# elif event.type == "logout":
#   if event.user in machines[event.machine]:
#     machines[event.machine].remove(event.user)
#return machines


def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lan'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#Absolutely, let's reframe the example using a more relatable scenario. Imagine we're organizing a party and we want to keep track of who arrives and leaves. Each person at the party is like an "attendee," and their actions are either "arriving" or "leaving."In this scenario, we're tracking attendees at a party. Each attendee has a name, and they can either "arrive" or "leave" different areas of the party, such as the backyard, living room, or kitchen. The `current_guests` function keeps track of who's at each location, and the `generate_report` function displays a list of guests at each location.This analogy makes the code more relatable by using a party context, where attendees correspond to users and their actions represent events.Here's the revised code with the party analogy:

class Attendee:
    def __init__(self, event_time, event_type, location, name):
        self.time = event_time
        self.type = event_type
        self.location = location
        self.name = name

def get_event_time(attendee):
    return attendee.time

def current_guests(attendees):
    attendees.sort(key=get_event_time)
    locations = {}
    for attendee in attendees:
        if attendee.location not in locations:
            locations[attendee.location] = set()
        if attendee.type == "arriving":
            locations[attendee.location].add(attendee.name)
        elif attendee.type == "leaving":
            locations[attendee.location].discard(attendee.name)
    return locations

def generate_report(locations):
    for location, guests in locations.items():
        if len(guests) > 0:
            guest_list = ", ".join(guests)
            print("{}: {}".format(location, guest_list))

attendees = [
    Attendee('2022-07-15 18:00', 'arriving', 'backyard', 'Alice'),
    Attendee('2022-07-15 18:15', 'arriving', 'living room', 'Bob'),
    Attendee('2022-07-15 18:30', 'leaving', 'backyard', 'Alice'),
    Attendee('2022-07-15 18:45', 'arriving', 'kitchen', 'Charlie'),
    Attendee('2022-07-15 19:00', 'arriving', 'living room', 'David'),
]

guests = current_guests(attendees)
print(guests)

generate_report(guests)







