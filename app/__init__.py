from flask import Flask
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)


    bootstrap.init_app(app)

    from app import routes
    routes.init_app(app) #Criando as rotas do app


    return app



