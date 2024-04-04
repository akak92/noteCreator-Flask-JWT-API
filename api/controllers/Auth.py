from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from api import db
from api.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        result = request.get_json()
        name = result['name']
        last_name = result['last_name']
        username = result['username']
        password = result['password']
        re_password = result['re_password']

        user = User.query.filter_by(username=username).first()
        if user is None:
            if password == re_password:
                user = User(name=name, last_name=last_name, username=username, password='')
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                response = {'message' : 'User created succesfully'}, 200
            else:
                response = {'message' : 'Password does not match'}, 400
        else:
            response = {'message' : 'Username already exists'}, 400
    except Exception as err:
        response = {'message': f'Unexpected error: {err}'}, 500
    return response

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        result = request.get_json()
        username = result['username']
        password = result['password']

        user = User.query.filter_by(username=username).first()
        if user is None:
            response = {'message' : 'User does not exists.'}, 404
        else:
            if not user.check_password(password):
                response = {'message' : 'wrong password.'}, 400
            else:
                access_token = create_access_token(identity={
                    'id_user' : user.id_user,
                    'username' : user.username,
                    'name' : user.name,
                    'last_name' : user.last_name
                })
                response = {
                    'message' : 'LogIn Succesfull',
                    'access_token' : access_token
                }, 200
    except Exception as err:
        response = {'message': f'Unexpected error: {err}'}, 500
    return response