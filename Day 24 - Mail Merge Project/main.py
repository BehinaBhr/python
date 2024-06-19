# TODO: Create a letter using starting_letter.txt
#  for each name in invited_names.txt
#  Replace the [name] placeholder with the actual name.
#  Save the letters in the folder "ReadyToSend".

# Hint1: file.readlines(): returns a list containing each line in the file as a list item.
# Hint2: string.replace(oldvalue, newvalue, count): replaces a specified phrase with another specified phrase.
# Hint3: string.strip(characters): removes any leading, and trailing whitespaces.
# Leading means at the beginning of the string, trailing means at the end.
# You can specify which character(s) to remove, if not, any whitespaces will be removed.

with open("Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()
    print(names_list)

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names_list:
        original_name = name.strip()
        new_letter = letter_contents.replace("[name]", original_name)
        # print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{original_name}.txt", "w") as complete_letter:
            complete_letter.write(new_letter)
