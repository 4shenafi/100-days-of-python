from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

def model_to_dict(model):
    return {column.name: getattr(model, column.name) for column in model.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record
@app.route('/random' , methods=['GET'])
def get_random_cafe():
    cafe = Cafe.query.order_by(db.func.random()).first()
    return jsonify(model_to_dict(cafe))

@app.route('/all', methods=['GET'])
def get_all_cafes():
    cafes = Cafe.query.all()
    return jsonify([model_to_dict(cafe) for cafe in cafes])

@app.route('/search')
def search():
    query_location = request.args.get('loc')
    cafe = Cafe.query.filter_by(location=query_location).first()
    if cafe:
        return jsonify(model_to_dict(cafe))
    else:
        return jsonify({"error": "Cafe not found"}), 404

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record

if __name__ == '__main__':
    app.run(debug=True)
