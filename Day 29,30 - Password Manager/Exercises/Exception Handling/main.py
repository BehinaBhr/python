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
split_name = [letter for letter in name]
print(split_name)

your_dict = {letter: nato_dict[letter] for letter in split_name}
print(your_dict)

another_your_dict = {letter: code for (letter, code) in nato_dict.items() if letter in split_name}
print(another_your_dict)
