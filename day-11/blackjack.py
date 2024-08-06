import os
import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def clear_screen():
    os.system('clear')
    
def Ublackjack(Ucard, cards):
    while True:
        if sum(Ucard) == 21:
            break
        hit = input("Would you want to add a card? (h: hit, s: stand) ")
        if hit == 'h':
            Ucard.append(random.choice(cards))
            print(f'Your cards: {Ucard}')
        elif sum(Ucard) > 21:
            if 11 in Ucard:
                index = Ucard.index(11)
                Ucard[index] = 1
            else:
                break
        elif hit == 's':
            break
    return sum(Ucard)

def Dblackjack(Dcard, cards):
    while sum(Dcard) < 17:
        Dcard.append(random.choice(cards))
    if sum(Dcard) > 21:
        if 11 in Dcard:
            index = Dcard.index(11)
            Dcard[index] = 1
    return sum(Dcard)

def play(Usum, Dsum):
    print(logo)
    if Usum > 21:
        return f"You = {Usum}\nDealer = {Dsum}\n\tYou Lose!"
    elif Dsum > 21:
        return f"You = {Usum}\nDealer = {Dsum}\n\tYou Won!"
    elif Usum > Dsum:
        return f"You = {Usum}\nDealer = {Dsum}\n\tYou Won!"
    elif Usum < Dsum:
        return f"You = {Usum}\nDealer = {Dsum}\n\tYou Lose!"
    else:
        return f"You = {Usum}\nDealer = {Dsum}\n\tDRAW"

def main():
    while True:
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        Ucard = [random.choice(cards), random.choice(cards)]
        Dcard = [random.choice(cards), random.choice(cards)]
        print(f'Your cards: {Ucard}')
        print(f'Dealer cards: [{Dcard[0]}, x]')

        Usum = Ublackjack(Ucard, cards)
        Dsum = Dblackjack(Dcard, cards)
        clear_screen()
        print(play(Usum, Dsum))
    
        choice = input("Would you like to continue? ('y' or 'n') ")
        if choice == 'y':
            clear_screen()
            continue
        elif choice == 'n':
            break
        else:
            print("Invalid input!\nThank you!")
            break

if __name__ == "__main__":
    main()
