import logging
from flask import Blueprint
from flask_restful import Api, Resource

class Home(Resource):

    @staticmethod
    def get():
        return {'message': 'Server Start'}