# Should display "Last year’s annual report will be released in March 2024"
# Should display "In May, the CEO will hold a conference"
# Should display "The convention is scheduled for June"

#False

def replace_date(schedule, old_date, new_date):

    if old_date in schedule:
        p = len(old_date)

        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
        return new_schedule
   
    return schedule
 
print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024")) 
# Should display "Last year’s annual report will be released in March 2024"
print(replace_date("In April, the CEO will hold a conference", "April", "May")) 
# Should display "In May, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June")) 
# Should display "The convention is scheduled for June"



#Correct 
def replace_date(schedule, old_date, new_date):

    if old_date in schedule:
        new_schedule = schedule.replace(old_date, new_date)
        return new_schedule
        
    
    return schedule

print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024")) 
print(replace_date("In April, the CEO will hold a conference", "April", "May")) 
print(replace_date("The convention is scheduled for October", "October", "June"))  





#What will happen to first cat?
def replace_ending(sentence, old, new):
     
    if sentence.endswith(old):
        i = len(old)
        new_sentence = sentence[:-i] + sentence[-i:].replace(old, new)
        return new_sentence

    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"
