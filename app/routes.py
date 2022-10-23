# The responsibility of this file is to define the endpoints
# Blueprint is a Flask class that provides a pattern for grouping related routes
# Flask will often refer to these routes using the word "view"


from flask import Blueprint, jsonify

class Book():
    def __init__ (self, id, name, author, genre, num_in_series=0):
        self.id = id
        self.name = name
        self.author = author
        self.genre = genre
        self.num_in_series = num_in_series

BOOKS = [
    Book(1, "Harry Potter", "JK Rowling", "Fantasy", 7),
    Book(2, "The Lord of the Rings", "JRR Tolkein", "Fantasy", 3),
    Book(3, "The Rise and Fall of the Dinosaurs", "Some Dude", "Nonfiction"),
    Book(4, "I Know Why the Caged Bird Sings", "Maya Angelou", "Memoir")

]


books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def get_all_books():
    result = []
    for book in BOOKS:
        result.append({
            "id": book.id,
            "title": book.name,
            "author": book.author,
            "genre": book.genre,
            "number in series": book.num_in_series
        })

    return jsonify(result)

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    #try:
    book_id = int(book_id)
    #except:
        #return {f"message":f"book {book_id} not found"}, 404

    for book in BOOKS:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.name,
                "author": book.author,
                "genre": book.genre,
                "number in series": book.num_in_series
            }
    return {f"message":f"book {book_id} not found"}, 404

