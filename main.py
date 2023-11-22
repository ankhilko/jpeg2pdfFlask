from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>free JPEG to PDF online converter</h1>"


@app.route('/startpage', methods=['GET'])
def startpage():
    form = request.form['file']

    return render_template('startpage.html', form=form)


@app.route('/hello')
def hello():
    return render_template('hello.html')

