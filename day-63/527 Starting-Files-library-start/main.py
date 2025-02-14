from flask import Flask, render_template, request, redirect, url_for
from db.main import db, add_book, read_books

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)

@app.route('/')
def home():
    all_books = read_books()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        add_book(new_book['title'], new_book['author'], new_book['rating'])
        return redirect(url_for('home'))
    return render_template("add.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

