# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

from .user_controller import *

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(InsertUser, '/insert', methods=['POST'], endpoint='insert')
api.add_resource(SelectUser, '/select', methods=['GET', 'POST'], endpoint='select')
api.add_resource(UpdateUser, '/update', methods=['POST'], endpoint='update')
api.add_resource(DeleteUser, '/delete', methods=['POST'], endpoint='delete')
