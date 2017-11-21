from flask import Flask
from flask_restful import Api, Resource, reqparse, http_status_message

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return http_status_message(200)


class Hello(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, default='World')

    def get(self):
        args = self.parser.parse_args()
        return 'Hello, {name}! Nice to meet you'.format(name=args['name'])


api.add_resource(Hello, '/hello', endpoint='hello')
