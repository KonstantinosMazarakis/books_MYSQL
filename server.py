from flask_app.controllers import authors
from flask_app.controllers import books
from flask_app.controllers import author_add_book
from flask_app.controllers import books_add_author
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)
