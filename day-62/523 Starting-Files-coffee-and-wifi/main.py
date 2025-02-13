from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Close Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[
        (1, '☕'), 
        (2, '☕☕'), 
        (3, '☕☕☕'), 
        (4, '☕☕☕☕'), 
        (5, '☕☕☕☕☕')
    ], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=[
        (1, '📶'), 
        (2, '📶📶'), 
        (3, '📶📶📶'), 
        (4, '📶📶📶📶'), 
        (5, '📶📶📶📶📶')
    ], validators=[DataRequired()])
    power_rating = SelectField('Power Rating', choices=[
        (1, '🔌'), 
        (2, '🔌🔌'), 
        (3, '🔌🔌🔌'), 
        (4, '🔌🔌🔌🔌'), 
        (5, '🔌🔌🔌🔌🔌')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        name = form.cafe.data
        location = form.location.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_rating = form.power_rating.data

        with open('cafe-data.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow([name, location, open_time, close_time, coffee_rating, wifi_rating, power_rating])
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    # Read the CSV file
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        
        # Read the header row
        headers = next(csv_data)
        
        # Convert rows into a list of dictionaries
        cafes = []
        for row in csv_data:
            cafe_dict = {headers[i]: row[i] for i in range(len(headers))}
            cafes.append(cafe_dict)
        
        # Debugging: Print the data to the console
        print(cafes)
    
    # Pass the data to the template
    return render_template('cafes.html', cafes=cafes, headers=headers)


if __name__ == '__main__':
    app.run(debug=True)
