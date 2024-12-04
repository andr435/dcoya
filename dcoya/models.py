from sqlalchemy import Column, DateTime, func, String, Integer, Text, ForeignKey
from sqlalchemy.orm import deferred, relationship
from app import db, bcrypt
from flask_jwt_extended import get_jwt_identity


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    password = deferred(Column(String(150), nullable=False))
    created_at = deferred(Column(DateTime, default=func.now()))
    last_login = deferred(Column(DateTime))
    posts = relationship('Post', back_populates='author', lazy=True)
    comments = relationship('Comment', back_populates='author', lazy=True)

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def __repr__(self):
        return f'<User id: {self.id}, username: {self.username}>'


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship('User', back_populates='posts', lazy=True)
    comments = relationship('Comment', back_populates='post', lazy=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<Post id: {self.id}, title: {self.title}>'

    def json(self):
        return {'id': self.id,
                'title': self.title,
                'body': self.body,
                'author': {
                    'id': self.author.id,
                    'username': self.author.username
                }
            }

    def json_with_comment(self):
        return {'id': self.id,
                'title': self.title,
                'body': self.body,
                'author': {
                    'id': self.author.id,
                    'username': self.author.username
                },
                'comment': [Comment.json(comment) for comment in self.comments],
                'created_at': self.created_at,
                'updated_at': self.updated_at
            }


class Like(db.Model):
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f'<Like id: {self.id}>'


class Comment(db.Model):
    id = Column(Integer, primary_key=True)
    body = Column(String(300), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship('Post', back_populates='comments', lazy=True)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship('User', back_populates='comments', lazy=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<Comment id: {self.id}>'

    def json(self):
        current_user_id = get_jwt_identity()
        return {'id': self.id,
                'body': self.body,
                'author': {
                    'id': self.author_id,
                    'author': self.author.username,
                    'owner': True if current_user_id and self.author_id == int(current_user_id) else False
                },
                'created_at': self.created_at,
                'updated_at': self.updated_at
            }
