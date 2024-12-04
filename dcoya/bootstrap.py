from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flasgger import Swagger

app = Flask(__name__)

# Init Config
app.config.from_object(Config)

# Init DB
db = SQLAlchemy(app)

# Init JWT
jwt = JWTManager(app)

# Init Bcrypt
bcrypt = Bcrypt(app)

# Init Swagger
swagger = Swagger(app)
