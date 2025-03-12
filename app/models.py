# Importa a classe UserMixin do flask_login para fornecer métodos padrão para autenticação de usuários
from flask_login import UserMixin
# Importa as instâncias do banco de dados (db) e do gerenciador de login (login_manager) do módulo atual
from . import db, login_manager

# Define a página de login padrão para usuários não autenticados
login_manager.login_view = 'main.login'


# Definição da classe User, que representa a tabela 'users' no banco de dados
class User(db.Model, UserMixin):  # Herda de db.Model para modelagem do banco e UserMixin para suporte ao login
    __tablename__ = 'users'  # Define o nome da tabela no banco

    # Definição das colunas da tabela
    id = db.Column(db.Integer, primary_key=True)  # Chave primária, identificador único
    name = db.Column(db.String(140), unique=True, nullable=False)  # Nome do usuário (único e obrigatório)
    email = db.Column(db.String(140), unique=True, nullable=False)  # E-mail (único e obrigatório)
    password = db.Column(db.String(250), nullable=False)  # Senha criptografada (obrigatória)

    # Método para representação textual do objeto User (usado para debugging)
    def __repr__(self):
        return f"<User {self.name}, {self.email}>"
    
    # Método para retornar os dados do usuário como um dicionário
    def asdict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

    # Relacionamento com a tabela Info (um usuário pode ter várias informações)
    infos = db.relationship('Info', backref='user', lazy=True)


# Definição da classe Info, que representa a tabela 'infos' no banco de dados
class Info(db.Model):
    __tablename__ = 'infos'  # Define o nome da tabela

    # Definição das colunas da tabela
    id = db.Column(db.Integer, primary_key=True)  # Chave primária
    name = db.Column(db.String(140), nullable=False)  # Nome (obrigatório)
    age = db.Column(db.String(100), nullable=False)  # Idade (obrigatória)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Chave estrangeira vinculada ao usuário

    # Método para representação textual do objeto Info
    def __repr__(self):
        return f"<Info {self.name}, {self.age}>"
    
    # Método para retornar os dados da informação como um dicionário
    def asdict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'user_id': self.user_id
        }


# Função para carregar um usuário pelo ID (usado pelo Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Busca o usuário no banco de dados pelo ID
