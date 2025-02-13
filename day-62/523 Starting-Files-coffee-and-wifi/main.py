from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Close Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', 
                                choices=['☕️', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'], 
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating',
                                choices=['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], 
                              validators=[DataRequired()])
    power_rating = SelectField('Power Rating', 
                                choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                                validators=[DataRequired()])

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
        name = request.form['cafe']
        location = request.form['location']
        open_time = request.form['open_time']
        close_time = request.form['close_time']
        coffee_rating = request.form['coffee_rating']
        wifi_rating = request.form['wifi_rating']
        power_rating = request.form['power_rating']

        file_path = os.path.join(os.path.dirname(__file__), 'cafe-data.csv')
        with open(file_path, mode='a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([name, location, open_time, close_time, coffee_rating, wifi_rating, power_rating])

        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    file_path = os.path.join(os.path.dirname(__file__), 'cafe-data.csv')
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.DictReader(csv_file, delimiter=',')
        list_of_rows = [row for row in csv_data]
    
    print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
