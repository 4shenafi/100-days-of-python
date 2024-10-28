import pandas as pd

dict_data = pd.read_csv("nato_phonetic_alphabet.csv")

user_input = input("Enter a word: ").upper()

list_of_words = [dict_data[dict_data["letter"] == letter]["code"].values[0] for letter in user_input]

print(list_of_words)
