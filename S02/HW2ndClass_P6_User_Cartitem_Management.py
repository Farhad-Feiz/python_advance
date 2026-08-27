from peewee import SqliteDatabase,Model,CharField,IntegerField,BooleanField,ForeignKeyField
# --------------------------------------
#        Database constructiom
# --------------------------------------
db = SqliteDatabase("cart.db")
# --------------------------------------
#        Creat User Class
# --------------------------------------
class User(Model):
    class Meta:
        database = db

    name = CharField()

# --------------------------------------
#        Creat Product Class
# --------------------------------------
class Product(Model):
    class Meta:
        database = db

    name        = CharField()
    price       = IntegerField()
    stock       = IntegerField()
    description = CharField()

# --------------------------------------
#        Creat CartItem Class
# --------------------------------------
class Cartitem(Model):
    class Meta:
        database = db

    quantity= IntegerField()
    user    = ForeignKeyField(User , backref= "cart")
    product = ForeignKeyField(Product, backref= "items")

db.connect()
# --------------------------------------
#        Create  Three Tables : 
# --------------------------------------
db.create_tables([User , Product , Cartitem])

# --------------------------------------
# 1.       Create  Some Users:
# --------------------------------------
u1 = User.create(name = "Rostam")
u2 = User.create(name = "Farhad")
u3 = User.create(name = "Helen")
u4 = User.create(name = "Behdad")
u5 = User.create(name = "Ali")
u6 = User.create(name = "Bijan")

# --------------------------------------
# 1.       Create  Some Products:
# --------------------------------------
p1 = Product.create(name = "Python Book",   price = 800000  ,stock = 200,description ="Great Book" )
p2 = Product.create(name = "Wireless Mouse",price = 1500000 ,stock = 150,description = "Easy to use")
p3 = Product.create(name = "Table Lamp",    price = 2000000 ,stock = 80 ,description = "Nice and cosy")
p4 = Product.create(name = "Ashtray",       price = 1800000 ,stock = 400,description = "Antique")
p5 = Product.create(name = "Mobile",        price = 5000000 ,stock = 300,description = "Special Offer!")
p6 = Product.create(name = "Apple Keyboard",price = 9000000 ,stock = 120,description = "Small and nice!")

# --------------------------------------
#        Create Cartitems
# --------------------------------------

Cartitem.create(user=u1, product=p1, quantity=2)
Cartitem.create(user=u1, product=p2, quantity=1)
Cartitem.create(user=u1, product=p3, quantity=3)
Cartitem.create(user=u1, product=p2, quantity=1)
Cartitem.create(user=u1, product=p3, quantity=3)
Cartitem.create(user=u2, product=p2, quantity=1)
Cartitem.create(user=u2, product=p3, quantity=3)
Cartitem.create(user=u2, product=p2, quantity=1)
Cartitem.create(user=u3, product=p3, quantity=3)
Cartitem.create(user=u2, product=p2, quantity=1)
Cartitem.create(user=u2, product=p3, quantity=3)
Cartitem.create(user=u2, product=p2, quantity=1)
Cartitem.create(user=u3, product=p3, quantity=3)
Cartitem.create(user=u2, product=p2, quantity=1)
Cartitem.create(user=u2, product=p3, quantity=3)
Cartitem.create(user=u2, product=p2, quantity=1)
Cartitem.create(user=u3, product=p3, quantity=3)


# ---------------------------------------------
# 2.       Show a Specific Cartitem  of a User:
# ---------------------------------------------

print("\nRostam's Cartitem : ")
for c in Cartitem.select().where(Cartitem.user == u1):
    print(c.product.name,"-----",c.product.price ,c.quantity)

# --------------------------------------
# 3.       Calculate a User Cartitem :
# --------------------------------------

total = 0

for item in Cartitem.select().where(Cartitem.user == u1):
    item_total = item.product.price * item.quantity

    print(
        "\nitem.product.name:",
        item.product.name,
        "--",
        item.product.price,
        "--x--",
        item.quantity,
        "====>",
        item_total
    )

    total += item_total

print("\nTotal amount:", total)
# --------------------------------------------
# 4.       Delete an Item From User Cartitem :
# --------------------------------------------
mouse = Cartitem.get((Cartitem.user== u1) & (Cartitem.product== p2))
mouse.delete_instance()
# --------------------------------------
# 5.       PART1 :
# --------------------------------------
for item in Cartitem.select().where(Cartitem.user== u1):
    if item.quantity > item.product.stock:
        print("\nError!!! Not Enough Stock for ",item.product.name)
    else:
        item.product.stock -= item.quantity
        item.product.save()

    item.delete_instance()
    print("Check Out Completed!!!")

# -----------------------------------------------
# 6.       Users with More Than n Items...n = 5 :
# -----------------------------------------------
for user in User.select():
    total_qty =  sum(item.quantity for item in user.cart)
    if total_qty > 5:
        print(user.name)

# --------------------------------------
# 7.       Best Sold Items :
# --------------------------------------
for product in Product.select():
    total_sold = sum(item.quantity for item in product.items)
    print(product.name,"-----",total_sold)



db.close()