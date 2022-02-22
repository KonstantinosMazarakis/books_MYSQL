from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.author import Author


@app.route("/")
def index():
    return redirect("/authors")

@app.route("/authors")
def authors():
    authors = Author.all_authors()
    return render_template("authors.html", authors = authors)

@app.route("/authors_add_post", methods=['POST'])
def authors_add_post():
    new_author = request.form
    Author.add_author(new_author)
    return redirect("/authors")
