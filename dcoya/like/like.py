from flask import Blueprint, jsonify, make_response
from post.post import post_bp
from models import Post, Like
from app import db
from swagger.like_swag import post_swag, delete_swag
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc, and_


like_bp = Blueprint('like', __name__)


@post_bp.route('/<int:post_id>/like', methods=['POST'], endpoint='new_like')
@jwt_required()
@swag_from(post_swag)
def new_like(post_id):
    current_user_id = int(get_jwt_identity())

    post = Post.query.get(post_id)

    if post is None:
        return make_response(jsonify({'message': f'post not found'}), 404)

    # check if user already liked this post
    like = Like.query.filter(and_(Like.post_id == post_id, Like.author_id == current_user_id)).first()

    if like:
        return make_response(jsonify({'message': 'Like already exists'}), 400)

    like = Like(post_id=post.id, author_id=current_user_id)

    try:
        db.session.add(like)
        db.session.commit()
    except exc.SQLAlchemyError:
        return make_response(jsonify({'message': f'Fail to create comment'}), 400)

    return make_response(jsonify({'message': f'Success'}), 200)


@like_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from(delete_swag)
def delete_like(id):
    like = Like.query.get(id)

    if like is None:
        return make_response(jsonify({'message': f'Like not found'}), 404)

    current_user_id = int(get_jwt_identity())

    if like.author_id != current_user_id:
        return make_response(jsonify({'message': f'Unauthorized'}), 401)

    try:
        db.session.delete(like)
        db.session.commit()
    except exc.SQLAlchemyError:
        return make_response(jsonify({'message': f'Fail to delete like'}), 400)

    return make_response(jsonify({'message': f'Success'}), 200)