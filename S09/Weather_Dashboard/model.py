from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    DateTimeField
)

from datetime import datetime

from config import DATABASE_NAME


db = SqliteDatabase(DATABASE_NAME)


class BaseModel(Model):

    class Meta:
        database = db


class SearchHistory(BaseModel):

    city_name = CharField()

    search_date = DateTimeField(
        default=datetime.now
    )


if __name__ == "__main__":

    db.connect()

    db.create_tables(
        [SearchHistory]
    )

    searches = SearchHistory.select()

    for search in searches:

        print(
            search.id,
            search.city_name,
            search.search_date
        )

    db.close()