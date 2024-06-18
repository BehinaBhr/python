#challenge 1
#Way 1:
#long
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years = []
for x in years:
    if x[-4:] == "2023":
        new = x.replace("2023","2024")
        updated_years.append(new)

    else:
        updated_years.append(x)
  
      
print(updated_years) 

#short
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

updated_years = [x.replace("2023","2024") if x[-4:] == "2023" else x for x in years]


print(updated_years) 


#Way 2:
#long
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years = []
for x in years:
    if x.endswith("2023"):
        new = x.replace("2023","2024")
        updated_years.append(new)

    else:
        updated_years.append(x)
  
      
print(updated_years) 

#shortt
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

updated_years = [x.replace("2023","2024") if x.endswith("2023") else x for x in years]


print(updated_years) 


#challenge 2
#long
def skip_elements(elements):

	result = []
	for index, element in enumerate (elements):
		if index % 2 == 0:
		   result.append(f"{element}")
	return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


#short
def skip_elements(elements):
	result = [x for index, x in enumerate (elements) if index % 2 == 0]
	return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) 
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) 







#challenge 3
def change_string(given_string):
    new_string = ""
    new_list = given_string.split()
  
    for element in new_list:
        new_string += element[1:] + "-"  + element[0] + " "

    return new_string


print(change_string("1one 2two 3three 4four 5five")) 
# Should print "one-1 two-2 three-3 four-4 five-5"  


print("//////////////////////////////////////////////////////")
#newchallenge 3
#long
def change_list(data):
    new_list = []
  
    for element in data.split():
        new_list.append(element[1:] + "-" + element[0] + " ")
    return new_list

print(change_list("1one 2two 3three 4four 5five")) 


# short 
def change_list(data):
    result = [element[1:] + "-" + element[0] + " " for element in data.split()]

    return result


print(change_list("1one 2two 3three 4four 5five")) 



print("------------------------------------------------")
#combine challenge 3 and newchallenge 3
def change_string_or_list(data):
    new_string = ""
    new_list = []
  
    for element in data.split():
        changed = element[1:] + "-" + element[0] + " "
        new_string += changed
        new_list.append(changed)
    return new_string, new_list


print(change_string_or_list("1one 2two 3three 4four 5five")) 

 






#challenge 4:
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = [x.replace("hpp","h") if x.endswith("hpp") else x for x in (filenames)]  
newfilenames = [x.replace("hpp","h") if x[-3:] == "hpp" else x for x in filenames]
print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]