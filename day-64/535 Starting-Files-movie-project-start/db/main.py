from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)

def add_movie(title, year, description, rating, ranking, review, img_url):
    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        rating=rating,
        ranking=ranking,
        review=review,
        img_url=img_url
    )
    db.session.add(new_movie)
    db.session.commit()

def read_movies():
    return Movie.query.all()


def update_movie(movie_id, new_ranking):
    movie_to_update = Movie.query.get(movie_id)
    movie_to_update.ranking = new_ranking
    db.session.commit()

def delete_movie(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    