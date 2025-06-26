from flask import request, jsonify
from app import app
from controller import get_all_books, add_book, get_book_by_id

@app.route("/")
def home():
    return "Welcome to the Library API"

@app.route("/books", methods=["GET"])
def list_books():
    books = get_all_books()
    return jsonify([{"id": book.book_id, "name": book.book_name} for book in books])

@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    if not data or "book_name" not in data:
        return jsonify({"error": "Missing book_name"}), 400
    book = add_book(data["book_name"])
    return jsonify({"id": book.book_id, "name": book.book_name}), 201

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        return jsonify({"id": book.book_id, "name": book.book_name})
    else:
        return jsonify({"error": "Book not found"}), 404
