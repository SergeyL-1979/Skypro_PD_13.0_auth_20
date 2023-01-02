#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import Resource, Namespace

from implemented import director_service
from dao.model.director import DirectorSchema

from decorators import auth_required
from decorators import admin_required

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):

    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did: int):
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404

    @auth_required
    @admin_required
    def put(self, did):
        req_json = request.json
        req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    @auth_required
    @admin_required
    def patch(self, did):
        req_json = request.json
        req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    @auth_required
    @admin_required
    def delete(self, did):
        director_service.delete(did)
        return "", 204
