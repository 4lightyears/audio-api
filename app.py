from flask import Flask
from flask_restful import Api

from resources.audio import AudioResource

app = Flask(__name__)
api = Api(app)

api.add_resource(AudioResource, '/audios')

if __name__ == '__main__':
    app.run(debug=True)
