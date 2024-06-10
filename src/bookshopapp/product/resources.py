from flask_restful import Resource
from .services import BookManger
from .repositories import BookRepository
from flask import jsonify 
from ..extensions import db
from .models import Category


class BookResource(Resource):
    def get(self):
        res = db.session.query(Category).all()
        result = [category for category in res]
        return jsonify(result[0])