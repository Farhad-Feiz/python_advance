from peewee import *
from datetime import datetime

from config import DATABASE_NAME

db = SqliteDatabase(DATABASE_NAME)

class BaseModel(Model):
    class Meta:
        database = db

class CryptoPrice(BaseModel):
    coin_name= CharField()
    price    = FloatField()
    timestamp= DateTimeField(default=datetime.now)

if __name__=="__main__":

    db.connect()

    db.create_tables([CryptoPrice])

    print("Database created successfully.")

    db.close()


