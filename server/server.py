'''
Run RESTful Flask server to receive requests from client
'''

from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask("name")
api = Api(app)

class Res(Resource):

    def get(self, payload):
        pass

    def post(self, payload):
        print(payload)

    def put(self, payload):
        pass

    def delete(self, payload):
        pass

api.add_resource(Res, "/arkac/<string:payload>")
app.run(host='0.0.0.0', debug=True) # Remove debug=True when finally deploying
