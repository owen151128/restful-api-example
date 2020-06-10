# -*- coding: utf-8 -*-

from app.db import marshmallow


class UserSchema(marshmallow.Schema):
    class Meta:
        fields = (
            'id', 'uid', 'name', 'age', 'timestamp'
        )


user_schema = UserSchema()
user_schemas = UserSchema(many=True)
