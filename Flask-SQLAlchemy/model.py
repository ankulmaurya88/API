from extensions import db 


# Base = declarative_base()

class Book(db.Model):
    __tablename__ = 'books'

    book_id =db. Column(db.Integer, primary_key=True)
    book_name =db. Column(db.String(90), nullable=False)


class Author(db.Model):
    __tablename__ = "author"

    author_id =db. Column(db.Integer, primary_key=True)
    author_name =db. Column(db.String, nullable=False)


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    user_name =db. Column(db.String, nullable=True)


class Cart(db.Model):
    __tablename__ = "cart"  # ✅ Corrected from __table__ to __tablename__

    cart_id = db.Column(db.Integer, primary_key=True)  # ✅ Fixed typo 'Intger'
    cart_number = db.Column(db.Integer)  # ✅ Fixed typo 'Intger'
