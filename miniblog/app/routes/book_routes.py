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

    book = Book.query.get(id_book)
    if book:
        return render_template('mylibrary.html', book=book)
    else:
        return "Book not found", 404

@app.route('/book_register', methods=['GET', 'POST'])
def book_register():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        year = request.form.get('year')
        user_id = session.get('user_id')

        new_book = Book(title=title, author=author, year=year, pages=pages, user_id=user_id)
        db.session.add(new_book)
        db.session.commit()
        flash('Livro cadastrado com sucesso!', 'success')
        return redirect(url_for('books'))

    return render_template('book_register.html')