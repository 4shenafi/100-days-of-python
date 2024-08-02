import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', 
           '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', 
           '_', '`', '{', '|', '}', '~']

password = []

print("\tWELCOME TO PYPASSWORD GENERATOR.")

no_letter = int(input("enter number of letters in your password: "))
no_numbers = int(input("enter number of numbers in your password: "))
no_symbols = int(input("enter number of symbols in your password: "))

for char in range(no_letter):
    password.append(random.choice(letters))
for int in range(no_numbers):
    password.append(random.choice(numbers))
for char in range(no_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
finalpassword = ''.join(password)

print("Your genrated password is: {}".format(finalpassword))
