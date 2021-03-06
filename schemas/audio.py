from mashmallow import Schema, fields

class SongSchema(Schema):
	class Meta:
		ordered = True

	id = fields.Int(dump_only=True)
	name = fields.String(required=True)
	duration = fields.Int(required=True)
	upload_time = fields.DateTime(dump_only=True)
	