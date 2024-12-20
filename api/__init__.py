from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    load_dotenv()
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")

    app = Flask(__name__)
    #app configuration
    app.config['SECRET_KEY'] = 'some-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"

    #jwt configuration
    app.config['JWT_SECRET_KEY'] = 'my-jwt-secret-key'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=12)

    jwt = JWTManager(app)

    from api.models import User, Note
    db.init_app(app)

    SWAGGER_URL = '/api/v1/swagger'
    API_URL = '/static/swagger.json'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config = {
            'app_name' : 'NoteCreation-Flask API'
        }
    )
    
    app.register_blueprint(SWAGGER_BLUEPRINT,url_prefix=SWAGGER_URL)
    from api.controllers.User import user_bp
    app.register_blueprint(user_bp, url_prefix='/api/v1')
    from api.controllers.Note import note_bp
    app.register_blueprint(note_bp, url_prefix='/api/v1')
    from api.controllers.Auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/v1')
    return app