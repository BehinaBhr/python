# import pandas
#
# # student_dict = {
# #     "student": ["Angela", "James", "Lily"],
# #     "score": [56, 76, 98]
# # }
# #
# # # Looping through dictionaries:
# # for (key, value) in student_dict.items():
# #     # Access key and value
#
# # # Loop through rows of a data frame
# # student_data_frame = pandas.DataFrame(student_dict)
# # for (index, row) in student_data_frame.iterrows():
# #     # Access index and row
# #     # Access row.student or row.score
#
# # # Dictionary Comprehension with a DataFrame:
# # # {new_key:new_value for (index, row) in data_frame.iterrows()}
# # new_dict = {row.student: row.score for (index, row) in student_data_frame.iterrows()}
# # print(new_dict)
#
# # TODO: Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
# nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
#
# # TODO: Create a list of the phonetic code words from a word that the user inputs.
# name = input("Enter a name: ").upper()
# code_words = [nato_dict[letter] for letter in name]
# print(code_words)
#
# split_name = [letter for letter in name]
# print(split_name)
#
# your_dict = {letter: nato_dict[letter] for letter in split_name}
# print(your_dict)
#
# another_your_dict = {letter: code for (letter, code) in nato_dict.items() if letter in split_name}
# print(another_your_dict)


#### Day 30  ####
import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}


def phonetic_generator():
    name = input("Enter a name: ").upper()
    try:
        code_words = [nato_dict[letter] for letter in name]
    except:
        print(" Sorry, Only letter is acceptable.")
        phonetic_generator()
    else:
        print(code_words)


phonetic_generator()



