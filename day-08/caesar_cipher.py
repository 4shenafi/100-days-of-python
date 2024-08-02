print("""
 ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗╚══███╔╝╚══███╔╝██╔══██╗██╔══██╗    ██╔════╝██║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██║     ███████║  ███╔╝   ███╔╝ ███████║██████╔╝    ██║     ██║██████╔╝█████╔╝ █████╗  ██████╔╝
██║     ██╔══██║ ███╔╝   ███╔╝  ██╔══██║██╔═══╝     ██║     ██║██╔═══╝ ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗███████╗██║  ██║██║         ╚██████╗██║██║     ██║  ██╗███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝          ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""")

def caesar_cipher(text, choice, step):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_text = []
    
    for letter in text:
        if letter.isalpha():
            is_upper = letter.isupper()
            letter = letter.lower()
            index = alphabet.index(letter)
            if choice == "encode":
                new_index = (index + step) % 26
            elif choice == "decode":
                new_index = (index - step) % 26
            new_letter = alphabet[new_index]
            if is_upper:
                new_letter = new_letter.upper()
            new_text.append(new_letter)
        else:
            new_text.append(letter)
    
    return "".join(new_text)

text = input("Enter the text: ")
choice = input("Enter 'encode' for encoding and 'decode' for decoding\nEnter: ").lower()
step = int(input("Enter the steps: "))

if choice in ["encode", "decode"]:
    result = caesar_cipher(text, choice, step)
    if choice == "encode":
        print(f'The encoded text is: {result}')
    else:
        print(f'The decoded text is: {result}')
else:
    print("Invalid choice. Please enter 'encode' or 'decode'.")
