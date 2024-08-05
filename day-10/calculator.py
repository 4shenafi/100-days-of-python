import sys

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def clear_lines(num_lines):
    """Clears a number of lines from the terminal."""
    for _ in range(num_lines):
        sys.stdout.write("\033[K")
        sys.stdout.write("\033[A")
        sys.stdout.flush()

def calculator(num1, operator, num2):
    """Performs the calculation based on the operator and returns the result as a string."""
    if operator == '+':
        return f'{num1} {operator} {num2} = {num1 + num2}'
    elif operator == '-':
        return f'{num1} {operator} {num2} = {num1 - num2}'
    elif operator == '*':
        return f'{num1} {operator} {num2} = {num1 * num2}'
    elif operator == '/':
        if num2 == 0:
            return "Denominator cannot be zero!"
        else:
            return f'{num1} {operator} {num2} = {num1 / num2}'
    else:
        return "Invalid Input!"

while True:
    print("Enter the operation in valid way (e.g., 2 + 5)")
    user_input = input("Enter: ")
    operation = user_input.split()
    
    if len(operation) != 3:
        print("Invalid input format. Please enter two numbers and an operator.")
        continue

    try:
        num1 = float(operation[0])
        op = operation[1]
        num2 = float(operation[2])
    except ValueError:
        print("Invalid numbers. Please enter valid numbers.")
        continue
    
    result = calculator(num1, op, num2)
    print(result)

    choice = input("Would you like to continue? (y/n): ").lower()
    if choice == 'n':
        break
    elif choice == 'y':
        clear_lines(4)
    elif choice != 'y':
        print("Invalid choice. Please enter 'y' or 'n'.")
        clear_lines(1)
