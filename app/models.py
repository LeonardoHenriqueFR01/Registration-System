from flask_login import UserMixin
from . import db, login_manager


login_manager.login_view = 'main.login'


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True, nullable=False)
    email = db.Column(db.String(140), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<User {self.name}, {self.email}>"
    
    def asdict(self):
        return {
            'id':self.id,
            'name':self.name,
            'email':self.email
        }
    
    infos = db.relationship('Info', backref='user', lazy=True)


class Info(db.Model):
    __tablename__ = 'infos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), nullable=False)
    age = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<Info {self.name}, {self.age}>"
    
    def asdict(self):
        return {
            'id':self.id,
            'name':self.name,
            'age':self.age,
            'user_id':self.user_id
        }


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
