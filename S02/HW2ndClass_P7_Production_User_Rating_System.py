from peewee import SqliteDatabase,Model,IntegerField,CharField,ForeignKeyField

# --------------------------------------
#        Database constructiom
# --------------------------------------
db =SqliteDatabase("rating.db")
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
#        Creat Rating Classo
# --------------------------------------
class Rating(Model):
    class Meta:
        database = db

    review    = CharField()
    score     = IntegerField()
    user      = ForeignKeyField(User, backref= "ratings")
    product   = ForeignKeyField(Product, backref= "ratings")

db.connect()
# --------------------------------------
#        Create  Three Tables : 
# --------------------------------------
db.create_tables([User , Product , Rating])

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
p7 = Product.create(name="Headphones",      price = 2500000 ,stock=50   , description= "No rating yet")

# ----------------------------------------------
#    Give Scores to Some Products bySome Users :
# ----------------------------------------------
Rating.create(user=u1, product=p1, score=5, review="Excellent book!")
Rating.create(user=u1, product=p2, score=4, review="Good mouse")
Rating.create(user=u2, product=p1, score=3, review="Not bad")
Rating.create(user=u2, product=p3, score=5, review="Great keyboard!")
Rating.create(user=u3, product=p2, score=2, review="Weak quality")
Rating.create(user=u3, product=p2, score=1, review="Crap")
Rating.create(user=u3, product=p3, score=3, review="So so")
Rating.create(user=u3, product=p3, score=4, review="Satisfying")
Rating.create(user=u3, product=p4, score=2, review="Rubbish")
Rating.create(user=u3, product=p4, score=3, review="Average")
Rating.create(user=u3, product=p5, score=2, review="Disaster")
Rating.create(user=u3, product=p6, score=2, review="Cheap")

# --------------------------------------
# 2.    Everu products Average :
# --------------------------------------
for product in Product.select():                                                
    if product.ratings.count() == 0:
        print("\nThere's no rating yet!!!")
    else:
        avg = (sum(r.score for r in product.ratings))/product.ratings.count()
        print(product.name," : ",avg)

# --------------------------------------
# 3.   Show specific User Comments:
# --------------------------------------
print("\nROSTAM Says:")
for r in Rating.select().where(Rating.user == u1):
    print(r.product.name,"---",r.score,"---",r.review)

print("\nFARHAD Says:")
for r in u2.ratings:
    print(r.product.name,"---",r.score,"---",r.review)
    
# -------------------------------------------
# 4.   Show Comments About a Specific Product:
# -------------------------------------------
for r in Rating.select().where(Rating.product == p2):
    print(r.user.name, "******",r.score, r.review)

for r in p3.ratings:
    print(r.user.name,"******",r.score, r.review)

# -------------------------------------------
# 5.   Show Products with No Score :
# -------------------------------------------
# print("\nProducts with no ratings:")
# for p in Product.select():
#     ratings = Rating.select().where(Rating.product == p)

#     if ratings.count()==0:
#         print(p.name)

print("\nProducts with no ratings:")

for p in Product.select():
    if p.ratings.count() == 0:
        print(p.name)
# -------------------------------------------
#  7.   Top 3 products by average rating :
# -------------------------------------------
print("\nAverage rating for each product:")

products_with_avg = []

for p in Product.select():
    if p.ratings.count() == 0:
        print(p.name, ": No ratings yet")
    else:
        avg = sum(r.score for r in p.ratings) / p.ratings.count()
        print(p.name, ":", avg)

products_with_avg.sort(key=lambda x: x[1], reverse=True)

for name, avg in products_with_avg[:3]:
    print(name, ":", avg)

db.close()