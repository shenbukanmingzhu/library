from flask import Blueprint, request, jsonify
from app import db
from app.models.borrow import BorrowRecord
from app.models.user import User
from app.models.book import Book
from datetime import datetime

borrow_bp = Blueprint('borrow_bp', __name__, url_prefix='/api/borrows')

# 借书
@borrow_bp.route('/borrow', methods=['POST'])
def borrow():
    data = request.json
    user = User.query.get(data.get('user_id'))
    book = Book.query.get(data.get('book_id'))
    if not user or not book:
        return jsonify({'msg': '用户或图书不存在'}), 404
    if book.stock <= 0:
        return jsonify({'msg': '库存不足'}), 400
    # 检查是否已借阅未还
    if BorrowRecord.query.filter_by(user_id=user.id, book_id=book.id, status='borrowed').first():
        return jsonify({'msg': '已借阅未还'}), 400
    # 创建记录+减库存
    new_borrow = BorrowRecord(user.id, book.id)
    book.stock -= 1
    db.session.add(new_borrow)
    db.session.commit()
    return jsonify(new_borrow.to_dict()), 201

# 还书
@borrow_bp.route('/return', methods=['POST'])
def return_book():
    data = request.json
    record = BorrowRecord.query.filter_by(
        user_id=data.get('user_id'),
        book_id=data.get('book_id'),
        status='borrowed'
    ).first()
    if not record:
        return jsonify({'msg': '无未还记录'}), 404
    # 更新状态+加库存
    record.status = 'returned'
    record.return_date = datetime.utcnow()
    book = Book.query.get(data.get('book_id'))
    book.stock += 1
    db.session.commit()
    return jsonify(record.to_dict())

# 查用户借阅记录
@borrow_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_borrows(user_id):
    if not User.query.get(user_id):
        return jsonify({'msg': '用户不存在'}), 404
    records = BorrowRecord.query.filter_by(user_id=user_id).all()
    return jsonify([r.to_dict() for r in records]), 200