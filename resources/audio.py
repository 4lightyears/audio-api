from flask_restful import Resource


class AudioResource(Resource):

    def get(self):
        return "Hello"
