from app import db


class UsersBooks(db.Model):
    __tablename__ = 'users_books'

    id_list = db.Column('id_list', db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id_user'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id_book'), nullable=False)

    def __repr__(self):
        return f'<UsersBooks id={self.id_list}, user_id={self.user_id}, book_id={self.book_id}>'

