from main import app


if __name__ == "__main__":

    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

# from python console do this to create the database
# from main import db
# from app import app
# app.app_context().push()
# db.create_all()
