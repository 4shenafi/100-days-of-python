from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/536304b9fcb8789cecd7'
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template('index.html', posts=blog_data['blogs'])

@app.route('/post/<int:post_id>')
def post(post_id):
    blog_url = 'https://api.npoint.io/536304b9fcb8789cecd7'
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    posts = blog_data['blogs']
    for post in posts:
        if post['id'] == post_id:
            return render_template('post.html', post=post)
if __name__ == "__main__":
    app.run(debug=True)
