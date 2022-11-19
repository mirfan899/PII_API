from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

from helpers import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./uploads"
api = Api(app, prefix="/api/v1")

parser = reqparse.RequestParser()
parser.add_argument('text', type=str, location='form')


class PII(Resource):
    def get(self):
        return {"message": "Welcome to PII API", "status": 200}

    def post(self):
        args = parser.parse_args()
        text = args['text']
        if text:
            return get_pii(text=text.rstrip())
        else:
            return {"Error": "File not supported or File not found"}


api.add_resource(PII, "/pii")

if __name__ == "__main__":
    app.run()
