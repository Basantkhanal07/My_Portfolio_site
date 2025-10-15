from flask import Flask, request, render_template_string
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/python/contact_form.py', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = EmailMessage()
    msg['Subject'] = f'New message from {name}'
    msg['From'] = email
    msg['To'] = 'your_email@example.com'
    msg.set_content(message)

    # Use Gmail SMTP or your host’s mail server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('your_email@example.com', 'your_app_password')
        smtp.send_message(msg)

    return render_template_string("<h1>Thank you, your message has been sent!</h1>")

if __name__ == "__main__":
    app.run(debug=True)
