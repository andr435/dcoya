class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://dcoya:dcoya123@postgres_container/dcoya'
    SECRET_KEY = 'app_secret_key'
    JWT_SECRET_KEY = 'jwt_secret_key'
    JWT_TOKEN_LOCATION = ['headers']
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    SWAGGER = {'title': 'Dcoya API'}
