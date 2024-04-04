from flask import Blueprint, request, jsonify, redirect, url_for
from flask_jwt_extended import create_access_token, jwt_required, unset_jwt_cookies
from api import db
from api.models import Note, User
from flask_jwt_extended import jwt_required, get_jwt_identity

note_bp = Blueprint('note', __name__)

@note_bp.route('/notes', methods=['GET'])
@jwt_required()
def get_notes():
    try:
        user_identity = get_jwt_identity()
        notes = Note.query.filter_by(id_user = int(user_identity.get('id_user'))).all()
        data = []
        for note in notes:
            data.append(note.serialize())
        response = data, 200
    except Exception as err:
        response = {'message': f'Unexpected error: {err}'}, 500
    return response

@note_bp.route('/notes/<id_note>', methods=['GET'])
@jwt_required()
def get_note(id_note):
    try:
        note = Note.query.filter_by(id_note=int(id_note)).first()
        if note is None:
            response = {'message' : 'Note not found'}, 404
        else:
            data = note.serialize()
            response = data, 200
    except Exception as err:
        response = {'message': f'Unexpected error: {err}'}, 500
    return response

@note_bp.route('/notes', methods=['POST'])
@jwt_required()
def create_note():
    try:
        user_identity = get_jwt_identity()
        result = request.get_json()
        id_user = user_identity.get('id_user')
        title = result['title']
        content = result['content']

        note = Note(id_user=int(id_user), title=title, content=content)
        db.session.add(note)
        db.session.commit()

        response = {'message' : 'Note created succesfully'}, 200
    except Exception as err:
        response = {'message': f'Unexpected error: {err}'}, 500
    return response

@note_bp.route('/notes', methods=['PATCH'])
@jwt_required()
def edit_note():
    try:
        result = request.get_json()
        id_note = result['id_note']
        title = result['title']
        content = result['content']

        note = Note.query.filter_by(id_note=int(id_note)).first()
        if note is None:
            response = {'message' : 'Note not found'}, 404
        else:
            note.title = title
            note.content = content
            db.session.commit()
            response = {'message' : 'Note edited succesfully'}, 200
    except Exception as err:
        response = {'message': f'Unexpected error: {err}'}, 500
    return response

@note_bp.route('/notes/<id_note>', methods=['DELETE'])
@jwt_required()
def delete_note(id_note):
    try:
        note = Note.query.filter_by(id_note=int(id_note)).first()
        if note is None:
            response = {'message' : 'Note not found'}, 404
        else:
            Note.query.filter_by(id_note=int(id_note)).delete()
            response = {'message' : 'Note deleted succesfully.'}, 200
    except Exception as err:
        response = {'message': f'Unexpected error: {err}'}, 500
    return response

