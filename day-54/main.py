# from flask import Flask

# # app = Flask(__name__)

# # @app.route("/")
# # def hello_world():
# #     return "Hello, World!"

# def add(a, b):
#     return a + b

# def substract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         print("error")
#     return a / b

# def calculator(calc_func, a, b):
#     return calc_func(a, b)

# # python function as first class object
# result = calculator(add, 10, 20)

# print(result)


# playing aroung function

def outer_function(function):
    def inner_function():
        print("Before")
        function()
        print("After")
    
    return inner_function

@outer_function
def middle_function():
    print("middle function")

the_middle_function = outer_function(middle_function)
