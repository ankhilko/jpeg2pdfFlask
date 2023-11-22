# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'free JPEG to PDF online converter'
#
#
# if __name__ == '__main__':
#     app.run()
#


# from flask import Flask
# from gevent.pywsgi import WSGIServer
#
# app = Flask(__name__)
#
# @app.route('/api', methods=['GET'])
# def index():
#     return "free JPEG to PDF online converter"
#
# if __name__ == '__main__':
#     # Debug/Development
#     # app.run(debug=True, host="0.0.0.0", port="5000")
#     # Production
#     http_server = WSGIServer(('', 5000), app)
#     http_server.serve_forever()


from main import app


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)


