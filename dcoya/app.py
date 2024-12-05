from bootstrap import app, db, bcrypt

if __name__ == '__main__':
    from routes import set_routes

    with app.app_context():
        set_routes()
        app.run(host='0.0.0.0', port=8000, use_reloader=True)
