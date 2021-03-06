from sqlalchemy.sql.schema import Column
from extensions import db
from sqlalchemy.dialects import postgresql


class AddRemove:
    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, audio_id):
        return cls.query.filter_by(id=audio_id).first()

class SongModel(db.Model, AddRemove):
    __tablename__ = "song"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    duration_seconds = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(
        db.DateTime(),
        nullable=False,
        server_default=db.func.now(),
        onupdate=db.func.now(),
    )


class PodcastModel(db.Model, AddRemove):
    __tablename__ = "podcast"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    duration_seconds = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(
        db.DateTime(),
        nullable=False,
        server_default=db.func.now(),
        onupdate=db.func.now(),
    )
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(postgresql.ARRAY(db.String, dimensions=1), nullable=False)


class AudiobookModel(db.Model, AddRemove):
    __tablename__ = "audiobook"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration_seconds = db.Column(db.Integer, nullable=False)
    upload_time = upload_time = db.Column(
        db.DateTime(),
        nullable=False,
        server_default=db.func.now(),
        onupdate=db.func.now(),
    )
