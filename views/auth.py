#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import Resource, Namespace, Api, reqparse

from implemented import auth_service

# ============ ИЛИ ============
# from container import auth_service

auth_ns = Namespace('auth')

# ===== ДЛЯ ПАРАМЕТРОВ В ВЕБ_ИНТЕРФЕЙСЕ FLASK-RESTX (swagger) API ======
api = Api()
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, help='Username')
parser.add_argument('password', type=str, help='Password')


@auth_ns.route('/')
class AuthView(Resource):
    @api.doc(parser=parser)
    def post(self):
        # data = request.json
        data = parser.parse_args()

        # username = data.get("username", None)
        # password = data.get("password", None)
        username = data["username"]
        password = data["password"]

        if None in [username, password]:
            return "", 400

        tokens = auth_service.generate_tokens(username, password)
        return tokens, 201

    def put(self):
        data = request.json
        token = data.get("refresh_token")

        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201

