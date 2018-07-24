from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)


class TodoItem(Resource):
    def get(self):
        # return {'task': 'Say "Hello, World!"'}
        return 'hello'


api.add_resource(TodoItem, '/')
app.register_blueprint(api_bp)



if __name__ == '__main__':
    app.run()