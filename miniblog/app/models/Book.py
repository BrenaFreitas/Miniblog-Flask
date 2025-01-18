from app import db


class Book(db.Model):
    __tablename__ = 'books'

    id_book = db.Column('id_book', db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    edition = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


