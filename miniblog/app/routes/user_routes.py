from app import app, db
from flask import render_template, request, flash, redirect, url_for, session
from flask_bcrypt import Bcrypt
from app.models import User,Book,UsersBooks # Certifique-se de que o modelo User esteja importado corretamente
from app.utils import autenticar_login  # Importa o decorador
from . import user_bp
from flask import request, jsonify


bcrypt = Bcrypt(app)

@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        

        user = User.query.filter_by(username_user=username).first()

        if user and bcrypt.check_password_hash(user.password_hash, password):
            session['username_user'] = username
            session['user_id'] = user.id_user
            flash('Login realizado com sucesso!', 'success')
            return render_template('index.html')

        else:
            flash('Credenciais inválidas')


    return render_template('login.html')

@app.route('/user_register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(username_user=username).first()

        if user:
            flash('Usuário já cadastrado')
        else:
            new_user = User(username_user=username, email_user=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Usuário cadastrado com sucesso!', 'success')
            return redirect(url_for('user_login'))

    return render_template('register.html')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    erro = None 
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        if USUARIOS.get(username) == password:
            session['username'] = username
            session['user_id'] = user.id_user

            flash('Login realizado com sucesso!', 'success')
            return render_template('index.html')
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')

    return render_template('login.html', erro=erro)

@app.route('/shop')
def shop():
    user_id = session.get('user_id')

    if not user_id:  
        flash('Você precisa estar logado para acessar esta página.', 'danger')
        return redirect(url_for('user_login'))

    
    return render_template('shop.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None) 
    flash('Você saiu com sucesso!', 'info')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register() :
    return render_template('register.html')

@app.route('/library', methods=['GET', 'POST'])
def library():
    return render_template('library.html')


@app.route('/book_register', methods=['GET', 'POST'])
def book_register():
    """Rota para cadastrar um novo livro"""

    user_id = session.get('user_id')

    if not user_id:  
        flash('Você precisa estar logado para acessar esta página.', 'danger')
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        year = request.form.get('year')
        price = request.form.get('price')
        edition = request.form.get('edition')

        if not title or not author or not year or not price or not edition:
            return jsonify({'message':' Todos os campos são obrigatórios!'}), 400

        new_book = Book(title=title, author=author, year=year,price=price, edition = edition)
        db.session.add(new_book)
        db.session.commit()

        new_user_book = UsersBooks(user_id=user_id, book_id=new_book.id_book)
        db.session.add(new_user_book)
        db.session.commit()
        flash('Livro cadastrado com sucesso!', 'success')
        return render_template('mylibrary.html')

    flash('Erro ao cadastrar livro', 'danger')
    return render_template('library.html')



@app.route('/book')
def books():
    """Rota para exibir todos os livros cadastrados"""
    page = request.args.get('page', 1, type=int) # Pega o número da página da URL
    per_page = 4  # Número de livros por página

    users_books = UsersBooks.query.paginate(page=page, per_page=per_page, error_out=False) # Paginação dos livros
     
    return render_template('mylibrary.html', users_books=users_books) # Renderiza o template com a lista de livros



@app.route('/user/<int:id_user>')
def user(id_user):
    """Rota para exibir os detalhes de um usuário"""
    user = User.query.get(id_user)
    
    if user:
        return render_template('mylibrary.html', user=user)
    else:
        return "User not found", 404

@app.route('/user_library')
def user_library():
    """Rota para exibir a biblioteca do usuário"""
    user_id = session.get('user_id')

    if not user_id:  
        flash('Você precisa estar logado para acessar esta página.', 'danger')
        return redirect(url_for('user_login'))

    user = User.query.filter(User.id_user == user_id).first()
    
    if not user: 
        flash('Usuário não encontrado.', 'danger')
        return redirect(url_for('user_login'))

    username = user.username_user
    email = user.email_user
    user_id = user.id_user

    page = request.args.get('page', 1, type=int)
    per_page = 4

    books_users_pagination = UsersBooks.query.filter_by(user_id=user_id).paginate(page=page, per_page=per_page, error_out=False)

    book_ids = [item.book_id for item in books_users_pagination.items]

    paginated_books = Book.query.filter(Book.id_book.in_(book_ids)).paginate(page=page, per_page=per_page, error_out=False)


    return render_template('mylibrary.html', books=books, user=user)


