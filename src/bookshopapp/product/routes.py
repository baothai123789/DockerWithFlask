from flask_restful import Api
from flask import Blueprint
from .resources import BookResource

blueprint = Blueprint('product',__name__)
api = Api(blueprint,prefix='/product')

api.add_resource(BookResource,'/getallbooks')
