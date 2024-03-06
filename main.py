import pandas

# Create a dictionary in this format using a for loop:
{"A": "Alfa", "B": "Bravo"}

file_path = "nato_phonetic_alphabet.csv"
# Create a dictionary from nato_phonetic_alphabet.csv using a for loop:

nato_phonetic_alphabet = pandas.read_csv(file_path)
nato_dict = {row.letter:row.code for (index, row) in nato_phonetic_alphabet.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic_code():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic_code()
    else:
        print(output_list)


generate_phonetic_code()
