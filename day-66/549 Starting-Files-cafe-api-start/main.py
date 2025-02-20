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
@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = request.args.get('new_price')
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify({"error": "Cafe not found"})

## HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if api_key != "secret":
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api-key."}), 403
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe."})
    else:
        return jsonify({"error": "Cafe not found"})
        
if __name__ == '__main__':
    app.run(debug=True)
