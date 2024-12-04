from flask import Blueprint, jsonify, request, make_response
from models import Post, Like
from app import db
from swagger.post_swag import get_swag, get_all_swag, put_swag, post_swag, delete_swag
from flasgger import swag_from
from sqlalchemy import desc
from flask_jwt_extended import jwt_required, get_jwt_identity
from validator.request import PostSchema, PostUpdateSchema
from sqlalchemy import exc, and_

post_bp = Blueprint('post', __name__)


@post_bp.route('/', methods=['GET'], endpoint='get_all')
@swag_from(get_all_swag)
def get_all():
    posts = Post.query.order_by(desc(Post.id)).all()
    return make_response([Post.json(post) for post in posts], 200)


@post_bp.route('/<int:id>', methods=['GET'], endpoint='get')
@jwt_required(optional=True)
@swag_from(get_swag)
def get(id):
    post = Post.query.get(id)

    if post is None:
        return make_response(jsonify({'message': f'post not found'}), 404)

    response = Post.json_with_comment(post)
    current_identity = get_jwt_identity()

    # add likes
    like_cnt = Like.query.filter(Like.post_id == post.id).count()

    like = Like.query.filter(
        and_(Like.post_id == post.id, Like.author_id == current_identity)).first()

    response['like'] = {'cnt': like_cnt,
                        'owner': True if like else False,
                        'like_id': like.id if like else -1
                        }

    if current_identity:
        owner = True if post.author_id == int(current_identity) else False
        response['owner'] = owner
    else:
        response['owner'] = False

    return make_response(response, 200)


@post_bp.route('/', methods=['POST'], endpoint='new_post')
@jwt_required()
@swag_from(post_swag)
def new_post():
    try:
        data = request.get_json()
    except:
        return make_response(jsonify({'message': 'Invalid Data'}), 400)

    errors = PostSchema().validate(data)

    if errors:
        return make_response(jsonify({'message': f'Invalid Data {errors}'}), 400)

    current_user_id = int(get_jwt_identity())

    post = Post(title=data['title'], body=data['body'], author_id=current_user_id)

    try:
        db.session.add(post)
        db.session.commit()
    except exc.SQLAlchemyError:
        return make_response(jsonify({'message': f'Fail to create post'}), 400)

    return make_response(jsonify({'message': f'Success'}), 200)


@post_bp.route('/<int:id>', methods=['PUT'], endpoint='put')
@jwt_required()
@swag_from(put_swag)
def put(id):
    try:
        data = request.get_json()
    except:
        return make_response(jsonify({'message': 'Invalid Data'}), 400)

    errors = PostUpdateSchema().validate(data)

    if errors:
        return make_response(jsonify({'message': f'Invalid Data {errors}'}), 400)

    current_user_id = int(get_jwt_identity())
    post = Post.query.get(id)

    if post is None:
        return make_response(jsonify({'message': f'post not found'}), 404)

    if post.author_id != current_user_id:
        return make_response(jsonify({'message': f'Unauthorized'}), 401)

    need_update = False
    if 'title' in data and len(data['title'].strip()) > 0:
        post.title = data['title'].strip()
        need_update = True

    if 'body' in data and len(data['body'].strip()) > 0:
        post.body = data['body'].strip()
        need_update = True

    if need_update:
        try:
            db.session.commit()
        except exc.SQLAlchemyError:
            return make_response(jsonify({'message': f'Fail to update post'}), 400)

        return make_response(jsonify({'message': f'Success'}), 200)

    return make_response(jsonify({'message': f'Invalid data'}), 400)


@post_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from(delete_swag)
def delete(id):
    post = Post.query.get(id)

    if post is None:
        return make_response(jsonify({'message': f'post not found'}), 404)

    current_user_id = int(get_jwt_identity())

    if post.author_id != current_user_id:
        return make_response(jsonify({'message': f'Unauthorized'}), 401)

    try:
        db.session.delete(post)
        db.session.commit()
    except exc.SQLAlchemyError:
        return make_response(jsonify({'message': f'Fail to delete post'}), 400)

    return make_response(jsonify({'message': f'Success'}), 200)