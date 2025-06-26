from flask import Flask
from extensions import db 
import model
import view

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app) 


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
