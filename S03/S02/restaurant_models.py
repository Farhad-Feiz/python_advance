from peewee import *

db = SqliteDatabase("restaurant.db")

class BaseModel(Model):
    class Meta:
        database = db

class Category(BaseModel):
    name = CharField()

class Food(BaseModel):
    name = CharField()
    price = IntegerField()
    category = ForeignKeyField(Category, backref="foods")


with db.connection_context():
    db.create_tables([Category, Food])
