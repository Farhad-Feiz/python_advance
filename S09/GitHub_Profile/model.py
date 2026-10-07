from peewee import*
from config import DATABASE_NAME

db = SqliteDatabase(DATABASE_NAME)

class BaseModel(Model):
    class Meta:
        database = db

class GithubUser(BaseModel):
    name = CharField()
    username = CharField(unique=True)
    followers_count = IntegerField()
    avatar_url = CharField()

if __name__== "__main__":
    
    db.connect()
    db.create_tables(
        [GithubUser]
    )
    print("Database created successfully.")
    db.close()

