from peewee  import  SqliteDatabase,ForeignKeyField,Model,CharField,BooleanField,IntegerField

db =SqliteDatabase("bank.db")

class Base(Model):
    class Meta:
        database=db
class Customer(Base):
    first_name=CharField()
    last_name =CharField()
    national_code=CharField(unique=True)
class Wallet(Base):
    balance=IntegerField(default=0)
    customer=ForeignKeyField(Customer,backref="wallets")
class Transaction(Base):
    amount=IntegerField()
    tx_type=CharField()
    wallet=ForeignKeyField(Wallet, backref="transactions")

with db.connection_context():
    db.create_tables([Customer,Wallet,Transaction])

