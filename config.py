# -*- coding: utf-8 _*_

import yaml
import os


class Config:
    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    LOG_PATH = os.path.abspath(APP_DIR) + os.sep + 'log'

    def __init__(self):
        self.config = None

    @staticmethod
    def parse_config(subject, config_yaml_path):
        with open(config_yaml_path) as c:
            config_yaml = yaml.load(c, yaml.FullLoader)
            for k, v in config_yaml.items():
                if k == subject:
                    if type(v) == dict:
                        return v
                    else:
                        print('option is None!')
                        raise IOError

    @staticmethod
    def apply_config(app, config):
        for k, v in config.items():
            app[k] = v
        app['SQLALCHEMY_DATABASE_URI'] = \
            f'mysql+pymysql://{config["DB_USERNAME"]}' \
            f':{config["DB_PASSWORD"]}' \
            f'@{config["DB_HOST"]}:{config["DB_PORT"]}/{config["DB_NAME"]}'
