# -*- coding: utf-8 -*-

import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from run import create_app
from app.db import db

app = create_app(os.path.abspath('config.yaml'))

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
