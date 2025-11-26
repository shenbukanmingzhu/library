from app import db
from datetime import datetime, timedelta

class BorrowRecord(db.Model):
    __tablename__ = 'borrow_records'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    borrow_date = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)  # 应还日期（借书后7天）
    return_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), default='borrowed')  # borrowed/returned

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = datetime.utcnow()
        self.due_date = self.borrow_date + timedelta(days=7)  # 7天期限

    def to_dict(self):
        # 判断是否逾期
        is_overdue = False
        if self.status == 'borrowed' and datetime.utcnow() > self.due_date:
            is_overdue = True
        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "borrow_date": self.borrow_date.strftime("%Y-%m-%d %H:%M:%S"),
            "due_date": self.due_date.strftime("%Y-%m-%d %H:%M:%S"),
            "return_date": self.return_date.strftime("%Y-%m-%d %H:%M:%S") if self.return_date else None,
            "status": self.status,
            "is_overdue": is_overdue
        }