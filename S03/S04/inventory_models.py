from peewee import CharField,SqliteDatabase,IntegerField,Model,ForeignKeyField

db = SqliteDatabase("shop.db")
class Base(Model):
    class Meta:
        database = db

class Product(Base):
    name =CharField()
    price=IntegerField()
    stock=IntegerField()

class Sale(Base):
    quantity = IntegerField()
    product  = ForeignKeyField(Product, backref="sales")

with db.connection_context():
    db.create_tables([Product,Sale])
