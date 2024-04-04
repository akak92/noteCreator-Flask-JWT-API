from flask import Blueprint, request
from api import db
from api.models import User
from flask_jwt_extended import jwt_required

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    try:
        users = User.query.all()
        data = []
        for user in users:
            data.append(user.serialize())
        response = data, 200
    except Exception as err:
        response = {'message': f'Unexpected error: {err}'}, 500
    return response

@user_bp.route('/users/<id_user>', methods=['GET'])
@jwt_required()
def get_user(id_user):
    try:
        user = User.query.filter_by(id_user=int(id_user)).first()
        if user is None:
            response = {'message' : 'User not found'}, 404
        else:
            data = user.serialize()
            response = data, 200
    except Exception as err:
        response = {'message': f'Unexpected error: {err}'}, 500
    return response

@user_bp.route('/users', methods=['PATCH'])
@jwt_required()
def edit_user():
    try:
        result = request.get_json()
        id_user = result['id_user']
        name = result['name']
        last_name = result['last_name']

        user = User.query.filter_by(id_user=int(id_user)).first()

        if user is None:
            response = {'message' : 'User not found'}, 404
        else:
            user.name = name
            user.last_name = last_name
            db.session.commit()
            response = {'message' : 'User edited succesfully'}, 200
    except Exception as err:
        response = {'message': f'Unexpected error: {err}'}, 500
    return response

@user_bp.route('/users/<id_user>', methods=['DELETE'])
@jwt_required()
def delete_user(id_user):
    try:
        user = User.query.filter_by(id_user=int(id_user)).first()
        if user is None:
            response = {'message' : 'User not found.'}, 404
        else:
            User.query.filter_by(id_user=int(id_user)).delete()
            response = {'message' : 'User deleted succesfully.'}, 200
    except Exception as err:
        response = {'message': f'Unexpected error: {err}'}, 500
    return response