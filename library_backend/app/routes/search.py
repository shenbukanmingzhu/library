from flask import Blueprint, request, jsonify
from app.models.book import Book

search_bp = Blueprint('search_bp', __name__, url_prefix='/api/search')

# 按条件搜索图书（支持书名、作者、分类）
@search_bp.route('/books', methods=['GET'])
def search_books():
    keyword = request.args.get('keyword', '')  # 搜索关键词
    category_id = request.args.get('category_id')  # 分类ID（可选）
    
    query = Book.query
    # 按关键词模糊查询（书名或作者）
    if keyword:
        query = query.filter(
            (Book.title.like(f'%{keyword}%')) | 
            (Book.author.like(f'%{keyword}%'))
        )
    # 按分类筛选
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    return jsonify([b.to_dict() for b in query.all()]), 200