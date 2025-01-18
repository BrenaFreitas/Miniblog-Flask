from app import app, db
from flask import render_template, request, flash, redirect, url_for, session
from flask_bcrypt import Bcrypt
from app.models import User  # Certifique-se de que o modelo User esteja importado corretamente
from app.utils import autenticar_login  # Importa o decorador

bcrypt = Bcrypt(app)

@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password_hash, password):
            session['username'] = username
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

        user = User.query.filter_by(username=username).first()

        if user:
            flash('Usuário já cadastrado')
        else:
            new_user = User(username=username, email=email)
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
            flash('Login realizado com sucesso!', 'success')
            return render_template('index.html')
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')

    return render_template('login.html', erro=erro)

@app.route('/shop')
@autenticar_login
def shop():
    return render_template('shop.html')

@app.route('/mylibrary')
@autenticar_login
def mylibrary():
    return render_template('mylibrary.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Você saiu com sucesso!', 'info')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register() :
    return render_template('register.html')
