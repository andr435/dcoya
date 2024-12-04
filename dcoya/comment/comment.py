from flask import Blueprint, jsonify, request, make_response
from post.post import post_bp
from models import Post, Comment
from app import db
from swagger.comment_swag import post_swag, put_swag, delete_swag
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from validator.request import CommentSchema
from sqlalchemy import exc


comment_bp = Blueprint('comment', __name__)


@post_bp.route('/<int:post_id>/comment', methods=['POST'], endpoint='new_comment')
@jwt_required()
@swag_from(post_swag)
def new_comment(post_id):
    try:
        data = request.get_json()
    except:
        return make_response(jsonify({'message': 'Invalid Data'}), 400)

    errors = CommentSchema().validate(data)

    if errors:
        return make_response(jsonify({'message': f'Invalid Data {errors}'}), 400)

    current_user_id = int(get_jwt_identity())

    post = Post.query.get(post_id)

    if post is None:
        return make_response(jsonify({'message': f'post not found'}), 404)

    comment = Comment(body=data['body'], post_id=post.id, author_id=current_user_id)

    try:
        db.session.add(comment)
        db.session.commit()
    except exc.SQLAlchemyError:
        return make_response(jsonify({'message': f'Fail to create comment'}), 400)

    return make_response(jsonify({'message': f'Success'}), 200)


@comment_bp.route('/<int:id>', methods=['PUT'], endpoint='update_comment')
@jwt_required()
@swag_from(put_swag)
def update_comment(id):
    try:
        data = request.get_json()
    except:
        return make_response(jsonify({'message': 'Invalid Data'}), 400)

    errors = CommentSchema().validate(data)

    if errors:
        return make_response(jsonify({'message': f'Invalid Data {errors}'}), 400)

    current_user_id = int(get_jwt_identity())
    comment = Comment.query.get(id)

    if comment is None:
        return make_response(jsonify({'message': f'post not found'}), 404)

    if comment.author_id != current_user_id:
        return make_response(jsonify({'message': f'Unauthorized'}), 401)

    if 'body' in data and len(data['body'].strip()) > 0:
        comment.body = data['body'].strip()
        try:
            db.session.commit()
        except exc.SQLAlchemyError:
            return make_response(jsonify({'message': f'Fail to update comment'}), 400)

        return make_response(jsonify({'message': f'Success'}), 200)

    return make_response(jsonify({'message': f'Invalid data'}), 400)


@comment_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from(delete_swag)
def delete_comment(id):
    comment = Comment.query.get(id)

    if comment is None:
        return make_response(jsonify({'message': f'comment not found'}), 404)

    current_user_id = int(get_jwt_identity())

    if comment.author_id != current_user_id:
        return make_response(jsonify({'message': f'Unauthorized'}), 401)

    try:
        db.session.delete(comment)
        db.session.commit()
    except exc.SQLAlchemyError:
        return make_response(jsonify({'message': f'Fail to delete post'}), 400)

    return make_response(jsonify({'message': f'Success'}), 200)