from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from datetime import timedelta

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) with credentials support
CORS(app, supports_credentials=True)

# Configure SQLAlchemy database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
# Disable SQLAlchemy event system for performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Set JWT secret key from environment variable
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
# Set JWT access token expiration time (default: 2 hours)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=int(os.getenv('JWT_EXPIRES_HOURS',2))) 

# Initia app(app)
db.init_app(app)
# Initialize JWT extension
jwt = JWTManager(app)

from routes.auth import auth_bp
from routes.openai import Prompt_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(Prompt_bp, url_prefix='/iraai')

with app.app_context():
    # Create all database tables
    db.create_all()



# Define a simple route for testing
@app.route("/")
def hello_world():
    return "<p>Hello, World! Updated</p>"