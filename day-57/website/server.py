from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<name>')
def guess(name):
    age_url = f'https://api.agify.io?name={name}'
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']

    gender_url = f'https://api.genderize.io?name={name}'
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data['gender']

    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/536304b9fcb8789cecd7'
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template('blog.html', posts=blog_data['blogs'])


if __name__ == '__main__':
    app.run(debug=True)