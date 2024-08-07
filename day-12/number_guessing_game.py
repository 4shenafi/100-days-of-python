import random

logo = r"""
    ╔╗╔┬ ┬┌┬┐┌┐ ┌─┐┬─┐  ┌─┐┬ ┬┌─┐┌─┐┌─┐┬┌┐┌┌─┐
    ║║║│ ││││├┴┐├┤ ├┬┘  │ ┬│ │├┤ └─┐└─┐│││││ ┬
    ╝╚╝└─┘┴ ┴└─┘└─┘┴└─  └─┘└─┘└─┘└─┘└─┘┴┘└┘└─┘
                ┌─┐┌─┐┌┬┐┌─┐                  
                │ ┬├─┤│││├┤                   
                └─┘┴ ┴┴ ┴└─┘                  

┬ ┬┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ┌┬┐┬ ┬┬┌─┐  ┌─┐┌─┐┌┬┐┌─┐         
│││├┤ │  │  │ ││││├┤    │ │ │   │ ├─┤│└─┐  │ ┬├─┤│││├┤          
└┴┘└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘   ┴ ┴ ┴┴└─┘  └─┘┴ ┴┴ ┴└─┘  o  o  o
"""
print(logo)

def game(level):
    num = random.randint(1, 100)
    for i in range(level):
        n = int(input("Enter Guessing number: "))    
        if n == num:
            print("You've got the right number!")
            break
        elif n > num:
            print("You're above the number!")
            print(f'You left {abs((i+1) - level)} attempts')
            continue
        elif n < num:
            print("You're below the number!")
            print(f'You left {abs((i+1) - level)} attempts')
            continue
    if n != num:
        print("You Loose!\nthe number was {}".format(num))
        
while True:
    choice = input("Please Enter The Dificulty Level ('hard' or 'easy'): ")
    if choice == "hard":
        game(5)
    elif choice == "easy":
        game(10)
    else:
        print("Invslid input!")
    
    ch = input("Would like to continue? ('y' or 'n'): ")
    if ch == 'y':
        continue
    else:
        break
