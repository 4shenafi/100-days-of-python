print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

choice = "yes"
participants = {}

while choice.lower() == "yes":
    name = input("What's your name? ")
    bid = int(input("Enter BID $"))
    participants[name] = bid
    choice = input("Would you like to add another student ('yes' or 'no'): ")
    if choice.lower() == "no":
        break

def find_highest(participants):
    highest = 0
    winner = None
    for key, bid in participants.items():
        if bid > highest:
            highest = bid
            winner = key
    return winner

winner = find_highest(participants)
if winner:
    print(f'The winner of the tender is: {winner}')
else:
    print("No participants were added.")
