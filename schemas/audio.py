from marshmallow import Schema, fields

class SongSchema(Schema):
	class Meta:
		ordered = True

	id = fields.Int(dump_only=True)
	name = fields.String(required=True)
	duration_seconds = fields.Int(required=True)
	upload_time = fields.DateTime(dump_only=True)


class PodcastSchema(Schema):
	class Meta:
		ordered = True

	id = fields.Int(dump_only=True)
	name = fields.String(required=True)
	duration_seconds = fields.Int(required=True)
	upload_time = fields.DateTime(dump_only=True)
	host = fields.String(required=True)
	participants = fields.List(fields.String(), required=True)


class AudioBookSchema(Schema):
	class Meta:
		ordered = True

	id = fields.Int(dump_only=True)
	title = fields.String(required=True)
	author = fields.String(required=True)
	narrator = fields.String(required=True)
	duration_seconds = fields.Int(required=True)
	upload_time = fields.DateTime(dump_only=True)