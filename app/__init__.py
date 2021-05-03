from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
login_manager = LoginManager()


bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "SECRET"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMT_TRACK_MODIFICATIONS"] = False


    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)


    from app import routes
    routes.init_app(app) #Criando as rotas do app


    return app



