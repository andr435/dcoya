from flask import Blueprint, jsonify, request, make_response
from flask_jwt_extended import create_access_token, jwt_required
from models import User
from app import bcrypt, db
from flasgger import swag_from
from validator.request import UserSchema
from swagger.auth_swag import signup_swag, login_swag
from sqlalchemy import exc, func
from sqlalchemy.orm import undefer


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['POST'])
@swag_from(signup_swag)
def signup():
    try:
        data = request.get_json()
    except:
        return make_response(jsonify({'message': 'Invalid Data'}), 400)

    errors = UserSchema().validate(data)

    if errors:
        return make_response(jsonify({'message': f'Invalid Data {errors}'}), 400)

    # check if username exists
    user = User.query.filter(User.username == data['username']).first()

    if user:
        return make_response(jsonify({'message': 'User already exists'}), 400)

    user = User(data['username'], data['password'])
    try:
        db.session.add(user)
        db.session.commit()
    except exc.SQLAlchemyError:
        return make_response(jsonify({'message': f'Fail to create user'}), 400)

    return make_response(jsonify({'message': f'Success'}), 200)


@auth_bp.route('/login', methods=['POST'])
@swag_from(login_swag)
def login():
    try:
        data = request.get_json()
    except:
        return make_response(jsonify({'message': 'Invalid Data'}), 400)

    errors = UserSchema().validate(data)

    if errors:
        return make_response(jsonify({'message': f'Invalid Data {errors}'}), 400)

    user = User.query.filter(User.username == data['username']).options(undefer(User.password)).first()

    if user is None:
        return make_response(jsonify({'message': 'User not found'}), 404)

    if bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=str(user.id))

        # update last login
        user.last_login = func.now()
        db.session.commit()

        return jsonify({'message': 'Login Success', 'access_token': f'Bearer {access_token}'})
    else:
        return jsonify({'message': 'Login Failed'}), 401
