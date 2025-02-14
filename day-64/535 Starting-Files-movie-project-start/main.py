from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from db.main import db, add_movie, read_movies, update_movie, delete_movie

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db.init_app(app)

@app.route("/")
def home():
    all_movies = read_movies()
    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        year = request.form["year"]
        description = request.form["description"]
        rating = request.form["rating"]
        ranking = request.form["ranking"]
        review = request.form["review"]
        img_url = request.form["img_url"]
        add_movie(title, year, description, rating, ranking, review, img_url)

        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    if request.method == "POST":
        new_ranking = request.form["ranking"]
        update_movie(movie_id, new_ranking)
        return redirect(url_for('home'))
    return render_template("edit.html", movie_id=movie_id)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    delete_movie(movie_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)