import os
from flask import Flask 
from .db import init_db
from . import routes


def create_app() -> Flask: 
    # Create and configure the app 

    app = Flask(__name__, 
                instance_relative_config=True
                )
    app.config.from_mapping(SECRET_KEY = 'dev', # Replace with env var or stronger key later
                            DATABASE="sqlite:///pizza.db"
                            )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('../instance/config.py')
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # Register routes
    app.register_blueprint(routes.bp)

    # # Initialize DB (optional, if using SQLite or simple structure for now)
    # init_db(app)


    return app 
