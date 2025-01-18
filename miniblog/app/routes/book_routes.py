from app import app, db
from flask import render_template, request, flash, redirect, url_for, session
from flask_bcrypt import Bcrypt
from app.models import User  # Certifique-se de que o modelo User esteja importado corretamente

bcrypt = Bcrypt(app)


@app.route('/book')
def books():
    books = Book.query.all()  # Consulta para pegar todos os livros
    return render_template('mylibrary.html', books=books)


@app.route('/book/<int:id_book>')
def book_details(id_book):
    # Consulta para pegar o livro pelo id
    book = Book.query.get(id_book)
    if book:
        return render_template('mylibrary.html', book=book)
    else:
        return "Book not found", 404