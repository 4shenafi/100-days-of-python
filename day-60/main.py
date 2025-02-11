from flask import Flask, render_template, request
from smtplib import SMTP, SMTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "ashenafipaul21@gmail.com"
receiver_email = "apawlos0@gmail.com"
password = ""  # Replace with your app password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        # Collect form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Send email
        try:
            with SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(sender_email, password)
                email_message = MIMEMultipart()
                email_message['From'] = sender_email
                email_message['To'] = receiver_email
                email_message['Subject'] = 'Contact Form Submission'
                body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
                email_message.attach(MIMEText(body, 'plain'))
                smtp.sendmail(sender_email, receiver_email, email_message.as_string())
            return 'Data received and email sent successfully!'
        except SMTPException as e:
            return f'Failed to send email: {str(e)}'
    return 'Invalid request method.'

if __name__ == '__main__':
    app.run(debug=True)