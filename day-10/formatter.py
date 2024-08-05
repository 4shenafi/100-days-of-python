fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

def formatter(first_name, last_name):
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return formatted_first_name, formatted_last_name

formatted_fname, formatted_lname = formatter(fname, lname)

print(f'The formatted name is: {formatted_fname} {formatted_lname}')
