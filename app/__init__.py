# -*- coding: utf-8 -*-

from flask import Flask

from . import api
from .api import models
from .db import db
from config import Config


def create_app(config_file_path):
    app = Flask(__name__)
    config = Config.parse_config('FLASK_CONFIG', config_file_path)
    Config.apply_config(app.config, config)

    db.init_app(app)
    api.init_app(app)

    return app
