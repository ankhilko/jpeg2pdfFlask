import os
import smtplib

import img2pdf
from flask import Flask, render_template, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userlist.db'
# Initialise the db
db = SQLAlchemy(app)


# Create a db model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id

#

subscribers = []


def date_turn():
    y = str(datetime.now().year).zfill(4)
    m = str(datetime.now().month).zfill(2)
    d = str(datetime.now().day).zfill(2)
    h = str(datetime.now().hour).zfill(2)
    mn = str(datetime.now().minute).zfill(2)
    s = str(datetime.now().second).zfill(2)
    ms = str(datetime.now().microsecond).zfill(4)

    return y + m + d + h + mn + s + ms


def converter_func(jpeg_path=os.getcwd(), output_path=os.getcwd(), file_name='file', format=None):
    dir_list = os.listdir(jpeg_path)
    start = 0
    if dir_list:
        for name in dir_list:
            if '.jpg' in name:
                start = 1
                break
    if start:
        file_path = f'{output_path}/{file_name}_{date_turn()}.pdf'

        if format in ['a4', 'A4']:
            layout = img2pdf.get_layout_fun((img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297)))
            with open(file_path, 'wb') as file:
                file.write(img2pdf.convert([f'{jpeg_path}/{page}' for page in dir_list if page.endswith('.jpg')], layout_fun=layout))
        else:
            with open(file_path, 'wb') as file:
                file.write(img2pdf.convert([f'{jpeg_path}/{page}' for page in dir_list if page.endswith('.jpg')]))


@app.route('/')
def index():
    title = 'JPG to PDF converter'
    return render_template('hello.html', title=title)


@app.route('/subcribe')
def subcribe():
    title = 'JPG to PDF converter'
    return render_template('subcribe.html', title=title)


@app.route('/form', methods=['POST'])
def form():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    # email = request.form['email']

    message = 'You have subscribed to my newsletter. Thank you!'
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls()
    server.login('ibotmailsuper@gmail.com', 'ubry qnqa pavf eiwj')
    server.sendmail('Admin', email, message)

    if not first_name or not last_name or not email:
        error_state = 'All fields are required...'
        return render_template('subcribe.html', error_state=error_state,
                               first_name=first_name,
                               last_name=last_name,
                               email=email)

    subscribers.append(f'{first_name} {last_name}, {email}')

    print(first_name)
    print(last_name)
    print(email)

    title = 'Thank you!'
    return render_template('form.html', title=title, subscribers=subscribers)


@app.route('/about')
def about():
    names = ['John', 'Mary', 'Barry', 'Mess']
    title = 'About Online-JPG-to-PDF-Converter'
    return render_template('about.html', names=names, title=title)


@app.route('/userlist', methods=['GET', 'POST'])
def userlist():

    if request.method == 'POST':
        users_name = request.form['name']
        new_user = Users(name=users_name)

        try:
            db.session.add(new_user)
            db.session.commit()
        except:
            return "Error adding user"

    names = ['John', 'Mary', 'Barry', 'Mess']
    title = 'UserList'

    users = Users.query.order_by(Users.date_created)

    return render_template('userlist.html', users=users, title=title)

