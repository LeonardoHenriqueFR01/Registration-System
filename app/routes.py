from flask import render_template, request, redirect, url_for, session, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from .models import User, db
from time import sleep


main = Blueprint('main', __name__)


# Rota para página principal
@main.route('/')
def home():
    return render_template('index.html')


# Rota para página apos fazer cadastro ou login
@main.route('/content')
def content():
    return render_template('content.html')


# Rota para fazer cadastro
@main.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    error_message = None

    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        user_exists = User.query.filter((User.name == name) | (User.email == email)).first()

        if user_exists:
            error_message = "Nome ou Email já cadastrados!"
            return render_template('index.html', error_cadastro=error_message)
        else:
            hash_password = generate_password_hash(password)
            user = User(name=name, email=email, password=hash_password)

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('main.content'))
    
    return render_template('index.html')


# Rota para fazer login
@main.route('/login', methods=['POST', 'GET'])
def login():
    error_message = None

    if request.method == 'POST':
        name = request.form.get('name_login')
        email = request.form.get('email_login')
        password = request.form.get('password_login')

        user_exists = User.query.filter_by(name=name, email=email).first()

        if user_exists and check_password_hash(user_exists.password, password):
            sleep(3)
            return redirect(url_for('main.content'))
        else:
            error_message = "Dados incorretos Tente novamente!"
            return render_template('index.html', error_login=error_message)
    
    return render_template('index.html')
