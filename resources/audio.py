from flask_restful import Resource
from flask import request, jsonify
from http import HTTPStatus


from models.audio import SongModel, PodcastModel, AudiobookModel, db

from schemas.audio import SongSchema, PodcastSchema, AudioBookSchema 

song_schema = SongSchema()
podcast_schema = PodcastSchema(many=True)
audiobook_schema = AudioBookSchema()

class AudioListResource(Resource):
	def post(self):
		audioType = request.headers.get('audioType')
		data = request.get_json()
		if audioType == 'Song':
			name = data.get('name')
			duration = data.get('duration_seconds')
			audio_data = SongModel(
				name=name,
				duration_seconds=duration
			)
		
		elif audioType == 'Podcast':
			name = data.get('name')
			duration = data.get('duration_seconds')
			host = data.get('host')
			participants = data.get('participants')
			audio_data = PodcastModel(
				name=name,
				duration_seconds=duration,
				host=host,
				participants=participants
			)

		elif audioType == 'Audiobook':
			title = data.get('title')
			author = data.get('author')
			narrator = data.get('narrator')
			duration = data.get('duration_seconds')
			audio_data = AudiobookModel(
				title=title,
				author=author,
				narrator=narrator,
				duration_seconds=duration
			)

		else:
			return {}, HTTPStatus.BAD_REQUEST
		audio_data.save()

		return {"message": "OK"}, HTTPStatus.OK

class GetAudioResource(Resource):
	def get(get, audioType, audio_id=None):
		audioType = audioType.capitalize()
		audio_id = audio_id
		if audio_id is None:
			if audioType == 'Song':
				query_data = SongModel.get_all()
				jsonified_data = song_schema.dump(query_data)
			elif audioType == 'Podcast':
				query_data = PodcastModel.get_all()
				jsonified_data = podcast_schema.dump(query_data)
			elif audioType == 'Audiobook':
				query_data = AudiobookModel.get_all()
				jsonified_data = audiobook_schema.dump(query_data)
			else:
				return {}, HTTPStatus.BAD_REQUEST

			return jsonified_data, HTTPStatus.OK

		else:
			if audioType == 'Song':
				query_data = SongModel.get_by_id(audio_id)
				jsonified_data = song_schema.dump(query_data)
			elif audioType == 'Podcast':
				query_data = PodcastModel.get_by_id(audio_id)
				jsonified_data = podcast_schema.dump(query_data)
			elif audioType == 'Audiobook':
				query_data = AudiobookModel.get_by_id(audio_id)
				jsonified_data = audiobook_schema.dump(query_data)
			else:
				return {}, HTTPStatus.BAD_REQUEST

			return jsonified_data, HTTPStatus.OK

		return {}, HTTPStatus.BAD_REQUEST