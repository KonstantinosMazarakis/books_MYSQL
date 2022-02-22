from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route("/book/<int:id>")
def book_add_author(id):
    books_with_authors = Book.books_favorites_authors({'id':id})
    unfavoreted_authors = Author.unfavorited_authors({'id':id})
    return render_template("books_add_author.html", books_with_authors = books_with_authors, unfavoreted_authors = unfavoreted_authors)

@app.route("/book/book_add_author_post", methods=['POST'])
def book_add_author_post():
    data = request.form
    Author.add_favorites(data)
    return redirect(f"/book/{data['book_id']}")