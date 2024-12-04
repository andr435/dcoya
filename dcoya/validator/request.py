from marshmallow import Schema, fields, validate

exclude_char = [' ', '\t', '\n']


class UserSchema(Schema):
    username = fields.String(required=True, validate=[validate.Length(max=10, min=3), validate.ContainsNoneOf(exclude_char, error="No white space allowed")])
    password = fields.String(required=True, validate=[validate.Length(max=15, min=8), validate.ContainsNoneOf(exclude_char, error="No white space allowed")])


class PostSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(max=200, min=3))
    body = fields.String(required=True, validate=validate.Length(min=50))


class PostUpdateSchema(Schema):
    title = fields.String(required=False, validate=validate.Length(max=200, min=3))
    body = fields.String(required=False, validate=validate.Length(min=50))


class CommentSchema(Schema):
    body = fields.String(required=False, validate=validate.Length(min=10))
