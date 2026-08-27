from peewee import BooleanField, CharField, IntegerField, Model, SqliteDatabase,ForeignKeyField


db = SqliteDatabase("music.db")

class Base(Model):
    class Meta:
        database = db

class Artist(Base):
    
    name = CharField()

class Song(Base):
    title = CharField()
    duration = IntegerField()
    artist= ForeignKeyField(Artist , backref="songs")

with db.connection_context():
    db.create_tables([Artist , Song])
