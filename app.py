from flask import Flask, jsonify, request, abort
from config import Config
from models import db, Book

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Bookstore API!"})

# GET /books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

# GET /books/<id>
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book.to_dict()), 200

# POST /books
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    title = data.get('title')
    author = data.get('author')
    price = data.get('price')
    in_stock = data.get('in_stock', True)

    # Validations
    if not title or not author:
        return jsonify({"error": "Title and author are required"}), 400
    if not isinstance(price, (int, float)) or price <= 0:
        return jsonify({"error": "Price must be a positive number"}), 400

    book = Book(title=title, author=author, price=price, in_stock=bool(in_stock))
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201

# PUT /books/<id>
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json()

    title = data.get('title', book.title)
    author = data.get('author', book.author)
    price = data.get('price', book.price)
    in_stock = data.get('in_stock', book.in_stock)

    if not title or not author:
        return jsonify({"error": "Title and author cannot be empty"}), 400
    if not isinstance(price, (int, float)) or price <= 0:
        return jsonify({"error": "Price must be positive"}), 400

    book.title = title
    book.author = author
    book.price = price
    book.in_stock = bool(in_stock)

    db.session.commit()
    return jsonify(book.to_dict()), 200

# DELETE /books/<id>
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"}), 200

# Global error handler
@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad Request"}), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run(debug=True)