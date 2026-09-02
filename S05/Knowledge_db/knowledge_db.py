from peewee import *
from datetime import datetime

db = SqliteDatabase("knowledge.db")

class Base(Model):
    class Meta:
        Database=db
class Book(Base):
    isbn=CharField()
    title=CharField()
    author=CharField()
    publish_year=CharField()
class Note(Base):
    content=TextField()
    created_at=DateTimeField(
        default=datetime.now
    )
    book=ForeignKeyField(
    Book,
    backref="notes"
    )
class Tag(Base):
    name=CharField(
        unique=True
        )
class NoteTag(Base):
    note = ForeignKeyField(
        Note,
        backref = "note_tags"
    )
    tag=ForeignKeyField(
        Tag,
        backref="tag_notes"
    )
def create_tables():
    db.connect(reuse_if_open=True)
    db.create_tables([
        Book,
        Note,
        Tag,
        NoteTag
    ])
    db.close()
    