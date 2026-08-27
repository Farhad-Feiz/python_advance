from peewee import BooleanField, CharField, IntegerField, Model, SqliteDatabase,ForeignKeyField,fn

db = SqliteDatabase("list.db")

class User(Model):
    class Meta:
        database = db

    name = CharField()
    email = CharField(unique=True)
    active = BooleanField(default=True)


class Order(Model):
    class Meta:
        database = db
        
    product_name = CharField()
    quantity = IntegerField()
    user = ForeignKeyField(User , backref="orders")

db.connect()

db.create_tables([User, Order])


"""
User.create(name="Ali", email="ali@python.com")
User.create(name="Helen", email="helen@python.com")
User.create(name="Rostam", email="rostam@python.com")
User.create(name="Farhad", email="farhad@python.com")
User.create(name="Faezeh", email="faezeh@python.com")
User.create(name="Firouzeh", email="firouzeh@python.com")
User.create(name="Neda", email="neda@python.com")
User.create(name="Lida", email="lida@python.com")
User.create(name="Mohsen", email="mohsen@python.com")
# User.create(name="Ali", email="ali2@python.com")
User.create(name="Ali", email="alimani@python.com")
User.create(name="Jasem", email="jasem@python.com")

"""
"""
u1= User.get(User.name == "Jasem")
Order.create(product_name = "Table lamp",quantity = 1000, user = u1 )
Order.create(product_name = "Curtains",quantity = 500, user = u1 )
Order.create(product_name = "Shoes",quantity = 400, user = u1 )


u1= User.get(User.name == "Helen")
Order.create(product_name = "Table lamp",quantity = 100, user = u1 )
Order.create(product_name = "Ash tray",quantity = 1400, user = u1 )
Order.create(product_name = "Torch",quantity = 1800, user = u1 )


u1= User.get(User.name == "Rostam")
Order.create(product_name = "Paper",quantity = 2000, user = u1 )
Order.create(product_name = "Glasses",quantity = 1200, user = u1 )
Order.create(product_name = "Mouse",quantity = 10000, user = u1 )

"""
j1 = User.get(fn.LOWER(User.name) == "jasem")

orders = Order.select().where(Order.user== j1)
for o in orders:
    print(o.product_name,o.quantity)

# for u in User.id():
#     print(u.id, u.name)

# orders = Order.select().where(Order.user == "Jasem")
for o in Order.select().where(Order.quantity>1):
    print(o.user.name,"===>",o.product_name,"===>", o.quantity)

for o in Order.select().where(Order.quantity== 1000):
    print(o.user.name,"=======>",o.quantity)


total_quantity = sum(o.quantity for o in Order)
print("Total quantity : ",total_quantity)


print(User._meta.fields)

db.close()