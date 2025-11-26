from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
from app.schemas.user import UserCreate
import hashlib  # 简单加密

user_bp = Blueprint('user_bp', __name__, url_prefix='/api/users')

# 注册
@user_bp.route('/register', methods=['POST'])
def register():
    try:
        data = UserCreate(**request.json)
    except ValueError as e:
        return jsonify({'msg': str(e)}), 400
    if User.query.filter_by(username=data.username).first():
        return jsonify({'msg': '用户名已存在'}), 400
    # 简单加密
    hashed_pwd = hashlib.md5(data.password.encode()).hexdigest()
    new_user = User(username=data.username, password=hashed_pwd)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

# 登录
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get('username')).first()
    if not user or user.password != hashlib.md5(data.get('password').encode()).hexdigest():
        return jsonify({'msg': '用户名或密码错误'}), 401
    return jsonify({'msg': '登录成功', 'user': user.to_dict()})

# 查询所有用户
@user_bp.route('', methods=['GET'])
def get_users():
    return jsonify([u.to_dict() for u in User.query.all()]), 200