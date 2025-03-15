# Importações necessárias para as funcionalidades do Flask e segurança
from flask import render_template, redirect, request, url_for, session, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User, Info  # Importa os modelos de banco de dados
from flask_login import login_user, login_required, current_user  # Para gerenciar login de usuário
from sqlalchemy import or_  # Para utilizar a operação 'OR' no filtro de consulta SQL
from time import sleep  # Importa sleep para atrasar a execução (simula um tempo de espera)

# Criação do blueprint 'main', que será usado para agrupar as rotas dessa parte do app
main = Blueprint('main', __name__)

# Rota para a página principal (página inicial do site)
@main.route('/')
def home():
    return render_template('index.html')  # Renderiza o template HTML para a página inicial


# Rota para página após o cadastro ou login (somente acessível para usuários logados)
@main.route('/content')
@login_required  # Garante que o usuário esteja logado para acessar essa rota
def sucess():
    users = Info.query.filter_by(user_id=current_user.id).all()  # Busca todas as informações do usuário logado
    return render_template('content.html', users=users)  # Renderiza a página de conteúdo e passa as informações do usuário


# Rota para a página de cadastro (criação de conta)
@main.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    error_message = None  # Inicializa uma variável para armazenar mensagens de erro

    if request.method == 'POST':  # Se o formulário foi enviado via POST
        name = request.form.get('name')  # Obtém o nome do usuário do formulário
        email = request.form.get('email')  # Obtém o e-mail do formulário
        password = request.form.get('password')  # Obtém a senha do formulário

        # Verifica se já existe um usuário com o mesmo nome ou e-mail
        user_by_name = User.query.filter_by(User.name == name)
        user_by_email = User.query.filter_by(User.email == email)

        if user_by_name:
            error_message = 'Nome já cadastrado!'
        
        elif user_by_email:
            error_message = 'Email já cadastrado!'

        if error_message:  # Se o usuário já existe, exibe uma mensagem de erro
            return render_template('index.html', error_cadastro=error_message)  # Retorna para a página inicial com o erro
        
        else:
            # Criptografa a senha antes de salvar no banco de dados
            hash_password = generate_password_hash(password, method='pbkdf2:sha256')

            # Cria um novo usuário e salva no banco de dados
            user = User(name=name, email=email, password=hash_password)
            db.session.add(user)
            db.session.commit()  # Comita a transação para salvar o novo usuário

            sleep(3)  # Aguarda 3 segundos (simula algum tempo de processamento)

            return redirect(url_for('main.sucess'))  # Redireciona para a página de sucesso
    
    return render_template('index.html', error=error_message)  # Retorna o template de cadastro com a mensagem de erro


# Rota para fazer login
@main.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None  # Inicializa uma variável para mensagens de erro

    if request.method == 'POST':  # Se o formulário foi enviado via POST
        name = request.form.get('name_login')  # Obtém o nome do formulário de login
        email = request.form.get('email_login')  # Obtém o e-mail do formulário de login
        password = request.form.get('password_login')  # Obtém a senha do formulário de login

        # Verifica se o usuário existe no banco de dados e a senha está correta
        user_exist = User.query.filter(User.name == name, User.email == email).first()

        if user_exist and check_password_hash(user_exist.password, password):  # Se usuário encontrado e senha válida
            sleep(3)  # Aguarda 3 segundos (simula algum tempo de processamento)
            login_user(user_exist)  # Realiza o login do usuário
            return redirect(url_for('main.sucess'))  # Redireciona para a página de sucesso
        else:
            error_message = 'Dados inválidos! Tente novamente.'  # Caso as credenciais estejam incorretas
            return render_template('index.html', error_login=error_message)  # Retorna à página de login com erro
        
    return render_template('index.html')  # Retorna o template de login


# Rota para cadastrar mais informações do usuário (após login)
@main.route('/cadastrar_user', methods=['GET', 'POST'])
@login_required  # Garante que o usuário esteja logado
def cadastrar_user():
    if request.method == 'POST':  # Se o formulário foi enviado via POST
        name = request.form.get('name')  # Obtém o nome do novo usuário a ser cadastrado
        age = request.form.get('age')  # Obtém a idade do novo usuário

        # Cria uma nova entrada na tabela 'Info' associada ao usuário logado
        new_info = Info(name=name, age=age, user_id=current_user.id)
        db.session.add(new_info)  # Adiciona a nova informação à sessão do banco
        db.session.commit()  # Comita a transação para salvar no banco

        sleep(2)  # Aguarda 2 segundos

        return redirect(url_for('main.sucess'))  # Redireciona para a página de sucesso
    
    return render_template('content.html')  # Retorna o template de conteúdo

# Rota para deletar informações de um usuário específico
@main.route('/deletar_user/<int:user_id>', methods=['POST'])
@login_required  # Garante que o usuário esteja logado
def deletar_user(user_id):
    # Verifica se o usuário logado tem permissão para deletar a informação do outro usuário
    user_info = Info.query.filter_by(id=user_id, user_id=current_user.id).first()

    if user_info:  # Se o usuário logado cadastrou essa informação, permite deletar
        db.session.delete(user_info)  # Deleta a informação do banco de dados
        db.session.commit()  # Comita a transação para salvar a remoção

        return redirect(url_for('main.sucess'))  # Redireciona para a página de sucesso
    else:
        return "Você não tem permissão para deletar esse usuário.", 403  # Caso o usuário tente deletar alguém que não cadastrou
