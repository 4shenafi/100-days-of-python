with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter_template = starting_letter.read()

with open("Input/Names/invited_names.txt", "r") as invited_names:
    list_of_names = invited_names.readlines()

for name in list_of_names:
    name = name.strip()
    personalized_letter = letter_template.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_to_{name}.txt", "w") as ready_to_send:
        ready_to_send.write(personalized_letter)