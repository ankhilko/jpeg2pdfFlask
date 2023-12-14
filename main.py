from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import smtplib


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userlist.db'
# Initialise the db
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id


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
    subscribers = []
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


@app.route('/updateuser/<int:id>', methods=['GET', 'POST'])
def updateuser(id):
    user_to_update = Users.query.get_or_404(id)

    if request.method == 'POST':
        user_to_update.name = request.form['name']
        try:
            db.session.commit()
            return redirect('/userlist')
        except:
            return "Error"

    title = 'User Edit'

    return render_template('updateuser.html', title=title, user_to_update=user_to_update)


@app.route('/deleteuser/<int:id>', methods=['GET', 'POST'])
def deleteuser(id):
    user_to_del = Users.query.get_or_404(id)
    try:
        db.session.delete(user_to_del)
        db.session.commit()
        return redirect('/userlist')
    except:
        return "Error"

