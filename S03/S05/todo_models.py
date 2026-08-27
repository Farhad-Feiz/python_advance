from peewee  import  SqliteDatabase,ForeignKeyField,Model,CharField,BooleanField,IntegerField

db = SqliteDatabase("task_manager.db")

class Base(Model):
    class Meta:
        database = db
class User(Base):
    username = CharField()
    password = CharField()
class Task(Base):
    title=CharField()
    is_done=BooleanField(default=False)
    user=ForeignKeyField(User,backref="tasks")
with db.connection_context():
    db.create_tables([User,Task])

