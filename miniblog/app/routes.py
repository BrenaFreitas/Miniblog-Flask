from app import app
from flask import render_template
from flask import request
from flask import redirect 
from flask import flash

@app.route('/')
@app.route('/index') 
def index():
    nome = 'Flask'
    dados = {'nome': 'Brena', 'idade': 21}
    return render_template('index.html', nome=nome,dados=dados)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/mylibrary')
def mylibrary():
    return render_template('mylibrary.html')

@app.route('/autenticar', methods=[ 'POST'])
def autenticar():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'admin' and password == 'admin':
        return redirect('/index')
    else:
        return redirect('/login')
    
