from app import app
from flask import render_template, request, redirect 
from flask import Flask, session, flash, url_for
from app.utils import autenticar_login  # Importa o decorador


# Usuário de teste
USUARIOS = {
    'admin': '1234'  # Nome de usuário: senha
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sobre')

def sobre():
    return render_template('sobre.html')


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
def shop():
    return render_template('shop.html')

@app.route('/mylibrary')
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