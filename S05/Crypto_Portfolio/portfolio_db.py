from peewee import SqliteDatabase,CharField,IntegerField,Model,FloatField,ForeignKeyField

db = SqliteDatabase("crypto.db")

class Base(Model):
    class Meta:
        database =db

class Asset(Base):
    symbol        = CharField(unique=True)
    total_amount  = FloatField(default=0)
    average_price = FloatField(default=0)

class TradeHistory(Base):
    asset      = ForeignKeyField(Asset, backref="trades")
    trade_type = CharField()
    amount     = FloatField()
    price      = FloatField()

db.connect()
db.create_tables([Asset,TradeHistory])

db.close()