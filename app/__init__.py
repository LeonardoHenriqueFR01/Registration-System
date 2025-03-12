from flask import Flask  # Importa a classe Flask para criar a aplicação web
from flask_sqlalchemy import SQLAlchemy  # Importa SQLAlchemy para manipulação do banco de dados
from flask_login import LoginManager  # Importa LoginManager para gerenciar autenticação de usuários

# Cria instâncias globais do banco de dados e do gerenciador de login
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)  # Inicializa a aplicação Flask

    # Configurações da aplicação
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Define o banco de dados SQLite
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa notificações de modificações do SQLAlchemy
    app.config['SECRET_KEY'] = 'dev'  # Define uma chave secreta para segurança da aplicação

    # Inicializa os componentes com a aplicação Flask
    db.init_app(app)  # Inicializa o banco de dados
    login_manager.init_app(app)  # Inicializa o gerenciador de login

    # Importa e registra as rotas da aplicação usando Blueprints
    from .routes import main
    app.register_blueprint(main)

    # Garante que as tabelas do banco de dados sejam criadas dentro do contexto da aplicação
    with app.app_context():
        db.create_all()

    return app  # Retorna a aplicação configurada
