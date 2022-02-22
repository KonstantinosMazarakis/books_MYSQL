from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import book

class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.on_books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def all_authors(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL('books_schema').query_db( query)
        authors = []
        for author in results:
            authors.append( Author(author) )
        return authors


    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES ( %(name)s, NOW() , NOW() );"
        return connectToMySQL('books_schema').query_db( query, data )

    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        return connectToMySQL('books_schema').query_db( query, data )


    @classmethod
    def authors_favorites_books(cls,data):
        query = "SELECT * FROM authors left join favorites ON favorites.author_id = authors.id left join books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db( query, data )
        author = Author(results[0])
        for row_from_db in results:
            book_data = {
            "id" : row_from_db["books.id"],
            "title" : row_from_db["title"],
            "num_of_pages" : row_from_db["num_of_pages"],
            "created_at" : row_from_db["books.created_at"],
            "updated_at" : row_from_db["books.updated_at"]
            }
            author.on_books.append(book.Book(book_data))
        return author


    @classmethod
    def add_favorites(cls,data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL('books_schema').query_db( query, data )
