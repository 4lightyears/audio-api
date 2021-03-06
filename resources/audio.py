from flask_restful import Resource
from flask import request, jsonify
from http import HTTPStatus
import json

from models.audio import SongModel, PodcastModel, AudiobookModel, db

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
		if audio_id is None:
			if audioType == 'Song':
				data = SongModel.get_all()
			elif audioType == 'Podcast':
				data = PodcastModel.get_all()
			elif audioType == 'Audiobook':
				data = AudiobookModel.get_all()
			else:
				return {}, HTTPStatus.BAD_REQUEST

			return json.dumps(data), HTTPStatus.OK

		else:
			if audioType == 'Song':
				data = SongModel.get_by_id()
			elif audioType == 'Podcast':
				data = PodcastModel.get_by_id()
			elif audioType == 'Audiobook':
				data = AudiobookModel.get_by_id()
			else:
				return {}, HTTPStatus.BAD_REQUEST

			return json.dumps(data), HTTPStatus.OK

		return {}, HTTPStatus.BAD_REQUEST