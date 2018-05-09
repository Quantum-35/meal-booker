from flask import Flask
from flask_restful import Api


# local imports
from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config= True)
