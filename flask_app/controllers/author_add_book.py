from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book



@app.route("/author/<int:id>")
def author_add_book(id):
    author_with_books = Author.authors_favorites_books({'id':id})
    unfavoreted_books = Book.unfavorited_books({'id':id})
    return render_template("author_add_book.html", author_with_books = author_with_books, unfavoreted_books = unfavoreted_books)

@app.route("/author/author_add_book_post", methods=['POST'])
def author_add_book_post():
    data = request.form
    Author.add_favorites(data)
    return redirect(f"/author/{data['author_id']}")