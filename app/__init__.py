import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Grab the DB string from the environment; fallback to a local sqlite file
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', 'sqlite:///local_test.db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Import and register routes
    from app.routes import bp
    app.register_blueprint(bp)

    return app

app = create_app()