'''
Run RESTful Flask server to receive requests from client
'''

from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient



app = Flask("name")
api = Api(app)
client = MongoClient()
db = client['attendance']


class Res(Resource):

    def get(self, payload):
        pass

    def post(self, payload):
        # Receiving a picture

        posts = db.posts
        post_data = {
            'name': payload[:-2],
            'entering': int(payload[-1:])
        }
        result = posts.insert_one(post_data)
        print('One post: {0}'.format(result.inserted_id))

    def put(self, payload):
        pass

    def delete(self, payload):
        pass

@app.route("/")
def test():
    return "Hello, World!"
api.add_resource(Res, "/arkac/<string:payload>")
app.run(host='0.0.0.0', debug=True) # Remove debug=True when finally deploying
