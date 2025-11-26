from app import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200))
    books = db.relationship('Book', backref='category', lazy=True)  # 关联图书

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "book_count": len(self.books)
        }