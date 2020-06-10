# -*- coding: utf-8 -*-

import os

from app import create_app

app = create_app(os.path.abspath('config.yaml'))

if __name__ == '__main__':
    app.run()
