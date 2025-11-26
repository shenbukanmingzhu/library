from flask import Blueprint, request, jsonify
from app import db
from app.models.category import Category

category_bp = Blueprint('category_bp', __name__, url_prefix='/api/categories')

# 创建分类
@category_bp.route('', methods=['POST'])
def create_category():
    data = request.json
    if not data.get('name'):
        return jsonify({'msg': '分类名称不能为空'}), 400
    if Category.query.filter_by(name=data['name']).first():
        return jsonify({'msg': '分类已存在'}), 400
    new_cat = Category(name=data['name'], description=data.get('description', ''))
    db.session.add(new_cat)
    db.session.commit()
    return jsonify(new_cat.to_dict()), 201

# 查询所有分类
@category_bp.route('', methods=['GET'])
def get_categories():
    return jsonify([c.to_dict() for c in Category.query.all()]), 200

# 按分类查图书
@category_bp.route('/<int:cat_id>/books', methods=['GET'])
def get_books_by_cat(cat_id):
    cat = Category.query.get(cat_id)
    if not cat:
        return jsonify({'msg': '分类不存在'}), 404
    return jsonify({
        'category': cat.name,
        'books': [b.to_dict() for b in cat.books]
    }), 200