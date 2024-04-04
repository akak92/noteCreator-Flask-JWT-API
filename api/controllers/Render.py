from flask import Blueprint, render_template

render_bp = Blueprint('render', __name__)

@render_bp.route('/login', methods=['GET'])
def login():
    try:
        response = render_template('login.html')
    except Exception as err:
        pass
    return response

@render_bp.route('/register', methods=['GET'])
def register():
    try:
        response = render_template('register.html')
    except Exception as err:
        pass
    return response

@render_bp.route('/panel', methods=['GET'])
def panel():
    try:
        response = render_template('panel.html')
    except Exception as err:
        pass
    return response