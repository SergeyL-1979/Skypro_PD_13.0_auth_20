#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import Resource, Namespace, Api

from implemented import user_service
from dao.model.user import UserSchema

from decorators import admin_required
from decorators import auth_required

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):
    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self):
        user_json = request.json
        user = user_service.create(user_json)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):

    def get(self, uid: int):
        try:
            user = user_service.get_one(uid)
            return user_schema.dump(user), 200
        except Exception as e:
            return str(e), 404

    def patch(self, uid):
        user_json = request.json
        user_json["id"] = uid
        user_service.update_partial(user_json)
        return "", 204

    # @auth_required
    @admin_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204


@user_ns.route('/<username>')
class UserView(Resource):
    def get(self, username):
        try:
            user_name = user_service.get_username(username)
            return user_schema.dump(user_name), 200
        except Exception as e:
            return str(e), 404

