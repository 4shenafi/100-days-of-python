from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


def add_book(title, author, rating):
    new_book = Book(title=title, author=author, rating=rating)
    db.session.add(new_book)
    db.session.commit()

def read_books():
    return Book.query.all()

# Use the application context
with app.app_context():
    db.create_all()