import random
Rock = '✊'
Paper = '✋'
Scissors = '✂️'

print("Enter your choice to play with computer.\n\t1. Rock\n\t2. Paper\n\t3. Scissors")
while True:
    user_input = int(input('CHOICE: '))
    if user_input == 1:
        user_input = Rock
    elif user_input == 2:
        user_input = Paper
    elif user_input == 3:
        user_input = Scissors
    else:
        print("user_inputvalid choice!")
    
    print("Your choice: {}".format(user_input))
    n = random.randint(1, 3)
    if n == 1:
        n = Rock
    elif n == 2:
        n = Paper
    elif n == 3:
        n = Scissors
    
    print("Computer's choice: {}".format(n))
    
    if user_input == 1 and n == 3:
        print("You wuser_input!")
    elif user_input == 2 and n == 1:
        print("You wuser_input!")
    elif user_input == 3 and n == 2:
        print("You wuser_input!")
    elif n == 1 and user_input == 3:
        print("Computer wuser_input!")
    elif n == 2 and user_input == 1:
        print("Computer wuser_input!")
    elif n == 3 and user_input == 2:
        print("Computer wuser_input!")
    else:
        print("Agauser_input")
        
    play_again = user_input("Do you want to play agauser_input? (yes/no): ").lower()
    if play_again != 'yes':
        break