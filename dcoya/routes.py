from auth.auth import auth_bp
from post.post import post_bp
from comment.comment import comment_bp
from like.like import like_bp
from app import app


def set_routes():
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(post_bp, url_prefix='/post')
    app.register_blueprint(comment_bp, url_prefix='/comment')
    app.register_blueprint(like_bp, url_prefix='/like')
