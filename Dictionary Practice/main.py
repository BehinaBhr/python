#dictionary.get(key, default)
student_scores = {'A': 8, 'B': 2, 'C': 7}
a_score = student_scores.get('A', 0)  # Returns 8
d_score = student_scores.get('D', 0)  # D is not in the dictionary, so returns 0
print(a_score)
print(d_score)


# Challenge 1 
def counter(text):
    result = {}
    for letter in text:
      
      if letter not in result:
          result[letter] = 0
      result[letter] += 1
      
    return result

print(counter("This is an example"))

#short
def counter(text):
    result = {}
    for letter in text:
        result[letter] = result.get(letter, 0) + 1
      
    return result

print(counter("This is an example"))


# Challenge 2
# This function receives a dictionary, which contains common employee last names as keys, and a list of employee first names as values. The function generates a new list that contains each employees’ fullname (First_name Last_Name). For example, the key "Garcia" with the values ["Maria", "Hugo", "Lucia"] should be converted to a list that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].


def list_full_names(dictionary):
    result = []
    for last, first in dictionary.items():
      print(f"{first} {last}")
      for name in first:
          result.append(name + " " + last)
        
    return result

print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']





# Challenge 3
# This function receives a dictionary, which contains resource categories (keys) with a list of available resources (values) for a company’s IT Department. The resources belong to multiple categories.The function should reverse the keys and values to show which categories (values) each resource (key) belongs to. 


def invert_resource_dict(dictionary):
    result = {}
    for categories, resources in dictionary.items():
        for resource in resources:
            
            if resource in result:
                result[resource].append(categories)
            else:
                result[resource] = [categories]
  
    return(result)


print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}



# Challenge 4
#long
def reset_scores(game_scores):
    new_game_scores = game_scores.copy() 
    for player, score in new_game_scores.items():
        new_game_scores[player] = 0
  
    return new_game_scores
 

game1_scores = {"Arshi": 3, "Catalina": 7, "Diego": 6}
print(reset_scores(game1_scores))
# Should print {'Arshi': 0, 'Catalina': 0, 'Diego': 0}

#short
def reset_scores(game_scores):
    result = {}
    # for player, score in game_scores.items():
    for player in game_scores:
        result[player] = result.get(player, 0)
  
    return result
 

game1_scores = {"Arshi": 3, "Catalina": 7, "Diego": 6}
print(reset_scores(game1_scores))