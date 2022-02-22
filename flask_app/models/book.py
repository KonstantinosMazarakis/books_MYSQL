import imp
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import author

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.on_authors = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def all_books(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL('books_schema').query_db( query)
        books = []
        for book in results:
            books.append( Book(book) )
        return books


    @classmethod
    def add_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES ( %(title)s, %(num_of_pages)s, NOW() , NOW() );"
        return connectToMySQL('books_schema').query_db( query, data )


    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        return connectToMySQL('books_schema').query_db( query, data )

    @classmethod
    def books_favorites_authors(cls,data):
        query = "SELECT * FROM books left join favorites ON favorites.book_id = books.id left join authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db( query, data )
        book = Book(results[0])
        for row_from_db in results:
            author_data = {
                "id" : row_from_db["authors.id"],
            "name" : row_from_db["name"],
            "created_at" : row_from_db["authors.created_at"],
            "updated_at" : row_from_db["authors.updated_at"]
            }
            book.on_authors.append(author.Author(author_data))
        return book

