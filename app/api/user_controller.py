# -*- coding: utf-8 -*-

import uuid

from flask import make_response
from flask import jsonify
from flask_restful import Resource, reqparse

from .models import User
from .schemas import user_schema, user_schemas

parser = reqparse.RequestParser()
parser.add_argument('uid', type=str)
parser.add_argument('name', type=str)
parser.add_argument('age', type=int)


def make_result(result, message):
    return jsonify({'data': result, 'message': message})


class InsertUser(Resource):
    body = str()
    status_code = int()

    def post(self):
        args = parser.parse_args()
        name = args['name']
        age = args['age']

        user = User(
            uid=uuid.uuid4().hex,
            name=name,
            age=age,
        )

        user.save()
        self.body = make_result(user_schema.dump(user), 'insert complete!')
        self.status_code = 200

        return make_response(self.body, self.status_code)


class SelectUser(Resource):
    body = str()
    status_code = int()

    def get(self):
        query = User.query.order_by('name').all()
        data = user_schemas.dump(query)

        self.body = make_result(data, 'select all complete!')
        self.status_code = 200

        return make_response(self.body, self.status_code)

    def post(self):
        args = parser.parse_args()
        name = args['name']
        query = User.query.filter_by(name=name)
        data = user_schemas.dump(query)

        self.body = make_result(data, 'select one complete!')
        self.status_code = 200

        return make_response(self.body, self.status_code)


class UpdateUser(Resource):
    body = str()
    status_code = int()

    def post(self):
        args = parser.parse_args()
        uid = args['uid']
        name = args['name']
        age = args['age']

        user = User.query.filter_by(uid=uid).first()
        if name:
            user.name = name
        if age:
            user.age = age
        User.update()
        data = user_schema.dump(user)

        self.body = make_result(data, 'update complete!')
        self.status_code = 200

        return make_response(self.body, self.status_code)


class DeleteUser(Resource):
    body = str()
    status_code = int()

    def post(self):
        args = parser.parse_args()
        uid = args['uid']

        User.query.filter_by(uid=uid).first().delete()

        self.body = make_result(None, 'delete complete!')
        self.status_code = 200

        return make_response(self.body, self.status_code)
