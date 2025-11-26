from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config  # 导入配置类

# 全局数据库对象（所有模型和路由共享）
db = SQLAlchemy()

def create_app():
    # 创建Flask应用实例
    app = Flask(__name__)
    # 加载配置（数据库连接、密钥等）
    app.config.from_object(Config)
    
    # 初始化数据库，绑定到当前应用
    db.init_app(app)
    
    # 导入所有蓝图（放在create_app内部避免循环导入）
    from app.routes.users import user_bp        # 用户模块蓝图
    from app.routes.books import book_bp        # 图书模块蓝图
    from app.routes.categories import category_bp  # 分类模块蓝图（关键！）
    from app.routes.borrows import borrow_bp    # 借阅模块蓝图
    from app.routes.search import search_bp      # 搜索模块蓝图
    
    # 注册所有蓝图（接口路径生效的关键）
    app.register_blueprint(user_bp)
    app.register_blueprint(book_bp)
    app.register_blueprint(category_bp)  # 必须注册分类蓝图，否则接口404
    app.register_blueprint(borrow_bp)
    app.register_blueprint(search_bp)
    
    # 在应用上下文里创建数据库表（首次运行时自动生成所有表）
    with app.app_context():
        db.create_all()
    
    return app