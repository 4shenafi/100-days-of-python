import random

levels = ["""
     |
     |
     |
     |
     |
=====
""",
"""
 +---+
     |
     |
     |
     |
     |
=====
""",
"""
 +---+
 |   |
     |
     |
     |
     |
=====
""",
"""
 +---+
 |   |
 O   |
/ \\  |
     |
     |
=====
""",
"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=====
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=====
"""
]

word_list = ["apple", "house", "window"]
chosen_word = random.choice(word_list)
space = ["_"] * len(chosen_word)
attempts = 0
max_attempts = len(levels) - 1

print(f'Chosen word: {chosen_word}')
print(" ".join(space))

while attempts < max_attempts and "_" in space:
    user_word = input("Enter a letter: ").lower()
    if user_word in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == user_word:
                space[index] = user_word
        print("Correct guess!")
    else:
        attempts += 1
        print(levels[attempts])
        print("Wrong guess!")

    print("".join(space))

if "_" not in space:
    print("Congratulations! You've won!")
else:
    print(f"Game over. The word was: {chosen_word}")
