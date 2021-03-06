from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from extensions import db

from config import Config

from resources.audio import AudioListResource, GetAudioResource

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)

	register_resource(app)
	register_extension(app)

	return app

def register_extension(app):
	db.init_app(app)
	migrate = Migrate(app, db)

def register_resource(app):
	api = Api(app)

	api.add_resource(AudioListResource, '/audio')
	api.add_resource(GetAudioResource, '/<string:audioType>', '/<string:audioType>/<int:audio_id>', endpoint='aud')

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)