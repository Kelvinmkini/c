from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Import and register blueprints
from app.routes.admin import admin_bp
from app.routes.client import client_bp
from app.routes.auth import auth_bp

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(client_bp, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/auth')