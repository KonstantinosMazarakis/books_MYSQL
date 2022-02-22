from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.book import Book


@app.route("/books")
def books():
    books = Book.all_books()
    return render_template("books.html", books = books)

@app.route("/books_add_post", methods=['POST'])
def books_add_post():
    new_book = request.form
    Book.add_book(new_book)
    return redirect("/books")
