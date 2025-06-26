from model import Book
from extensions import db

def get_all_books():
    return Book.query.all()


def add_book(book_name):
    new_book =Book(book_name=book_name)
    db.seesion.add(new_book)
    db.session.commit()
    return new_book


def get_book_by_id(book_id):
    return Book.query.get(book_id)