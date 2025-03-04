from flask import render_template, redirect, request, url_for, session, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User, Info
from flask_login import login_user, login_required, current_user
from sqlalchemy import or_


main = Blueprint('main', __name__)

# Rota para página principal
@main.route('/')
def home():
    return render_template('index.html')


# Rota para página apos fazer cadastro ou login
@main.route('/content')
@login_required
def sucess():
    users = Info.query.filter_by(user_id=current_user.id).all()
    return render_template('content.html', users=users)


# Rota para fazer cadastro
@main.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    error_message = None

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Verifica se o usuário já existe pelo nome ou email
        user_exists = User.query.filter(or_(User.name == name, User.email == email)).first()

        if user_exists:
            error_message = "Nome ou Email já cadastrado! Tente novamente"
            return render_template('index.html', error_cadastro=error_message)
        
        else:
            # Criptografa a senha antes de salvar no banco
            hash_password = generate_password_hash(password, method='pbkdf2:sha256')

            user = User(name=name, email=email, password=hash_password)

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('main.sucess'))
    
    return render_template('index.html', error=error_message)


# Rota para fazer login
@main.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None

    if request.method == 'POST':
        name = request.form.get('name_login')
        email = request.form.get('email_login')
        password = request.form.get('password_login')

        user_exist = User.query.filter(User.name == name, User.email == email).first()

        if user_exist and check_password_hash(user_exist.password, password):
            login_user(user_exist)
            return redirect(url_for('main.sucess'))
        else:
            error_message = 'Dados inválidos! Tente novamente.'
            return render_template('index.html', error_login=error_message)
        
    return render_template('index.html')


# Rota para fazer cadastro de usuários
@main.route('/cadastrar_user', methods=['GET', 'POST'])
@login_required
def cadastrar_user():
    
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        new_info = Info(name=name, age=age, user_id=current_user.id)
        db.session.add(new_info)
        db.session.commit()

        return redirect(url_for('main.sucess'))
    
    return render_template('content.html')
