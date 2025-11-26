from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # 存储加密后的密码
    role = db.Column(db.String(20), default='reader')  # reader/admin
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    max_borrow_limit = db.Column(db.Integer, default=5, nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role,
            "max_borrow_limit": self.max_borrow_limit,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
    