from flask import Flask, jsonify

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>' 
    return wrapper

def make_emphesized(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper

def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper

@app.route('/')
@make_bold
@make_emphesized
@make_underlined

def welcome():
    return 'Hello, World!'

@app.route('/<name>/<int:age>')
def greet(name, age):
    return f'Hello {name}, I think you are {age} years old!'

@app.route('/bye')
def say_bye():
    return 'Good bye have a nice time!'

if __name__ == '__main__':
    app.run(debug=True)