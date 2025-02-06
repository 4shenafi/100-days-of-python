from flask import Flask

app = Flask(__name__)

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

# Decorator function
def logging_decorator(function):
    def wrapper(user, *args, **kwargs):  # Explicitly naming 'user' for clarity
        if user.is_logged_in:
            return function(user, *args, **kwargs)  # Pass all arguments
        return 'You are not logged in!'
    return wrapper

# Applying the decorator
@logging_decorator
def say_hello(user):
    return f'Hello {user.name}'

# Creating a user instance
new_user = User('John')
new_user.is_logged_in = True  # Logging in

# Calling the function
print(say_hello(new_user))  # ✅ Output: Hello John

# Testing when not logged in
new_user.is_logged_in = False
print(say_hello(new_user))  # ✅ Output: You are not logged in!
