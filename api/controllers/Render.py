from flask import Blueprint, render_template, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
render_bp = Blueprint('render', __name__)

@render_bp.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@render_bp.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@render_bp.route('/panel/check', methods=['GET'])
@jwt_required()
def panel_check():
    return redirect(url_for('render.panel'))

@render_bp.route('/panel', methods=['GET'])
def panel():
    return render_template('panel.html')