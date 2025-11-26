from flask import Blueprint, request, jsonify
from app import db
from app.models.book import Book
from app.schemas.book import BookCreate

book_bp = Blueprint('book_bp', __name__, url_prefix='/api/books')

# 新增图书
@book_bp.route('', methods=['POST'])
def add_book():
    try:
        data = BookCreate(** request.json)
    except ValueError as e:
        return jsonify({'msg': str(e)}), 400
    if Book.query.filter_by(isbn=data.isbn).first():
        return jsonify({'msg': 'ISBN已存在'}), 400
    new_book = Book(
        title=data.title,
        author=data.author,
        isbn=data.isbn,
        stock=data.stock,
        category_id=data.category_id,
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

# 查询所有图书
@book_bp.route('', methods=['GET'])
def get_books():
    return jsonify([b.to_dict() for b in Book.query.all()]), 200