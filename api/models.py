from api import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'User'  # Specify the table name explicitly
    id_user = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256))

    #password-hashing generator (SHA-256 w/salting)
    def set_password(self, password):
        self.password = generate_password_hash(password)

	#password-hashed check(SHA-256 w/salting)
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def serialize(self):
        return {
            'id_user' : self.id_user,
            'name' : self.name,
            'username' : self.username,
            'password' : self.password

        }

class Note(db.Model):
    __tablename__ = 'Note'  # Specify the table name explicitly
    id_note = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer(), db.ForeignKey('User.id_user'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.String(1024))

    def serialize(self):
        return {
            'id_note' : self.id_note,
            'id_user' : self.id_user,
            'title' : self.title,
            'content' : self.content
        }