from peewee import CharField, ForeignKeyField, IntegerField, Model, SqliteDatabase

# --------------------------------------
# 1.  Database constructiom
# --------------------------------------

db = SqliteDatabase("retaurant.db")

# --------------------------------------
# 2-3-4.  Model Construction ---&---ForeignKeyField
# --------------------------------------

class Category(Model):
    
    name = CharField()

    class Meta:
        database = db

class Food(Model):

    name = CharField()
    price = IntegerField()
    category = ForeignKeyField(Category, backref="foods")

    class Meta:
        database =db

db.connect()

# --------------------------------------
# 5.  Creating Tables :
# --------------------------------------

db.create_tables([Category , Food])

# --------------------------------------
# 6. Creating  3 food categories :
# --------------------------------------

c1 = Category.create(name = "Appetizer")
c2 = Category.create(name = "Main course")
c3 = Category.create(name = "Dessert")

# --------------------------------------
# 7.  Finding The Main Course Section :
# --------------------------------------

main = Category.get(name = "Main course")

# --------------------------------------
# 8.  Creating a new food :
# --------------------------------------

Food.create(name = "Kabab", price = 450000, category = main)

# --------------------------------------------------------------------
# 9.  Creating 2 types of food and allocating them to othe food types :
# --------------------------------------------------------------------

Food.create(name = "Creme Brulee", price = 250000 , category = c3)
Food.create(name = "Chocolate Cake", price = 245000 , category = c3)
Food.create(name = "Stuffed Mushroom" , price = 150000 , category =c1)

# ---------------------------------------------------------
# 10.  Printing all food titles using select() and loop for:
# ---------------------------------------------------------

print("\n All Foods : *******")
for fn in Food.select():
    print(fn.name)

# ---------------------------------------------------------
# 11.  Printing foods that cost more than 150000:
# ---------------------------------------------------------

print("\n Foods more expensive than 150000 : *****")
for fn in Food.select().where(Food.price >= 150000):
    print(fn.name , fn.price)

# ---------------------------------------------------------
# 12.  Counting & Printing all food types:
# ---------------------------------------------------------
print(Category.select().count())

# ---------------------------------------------------------
# 13.  Find a specific food and call its food category:
# ---------------------------------------------------------

item = Food.get(Food.name == "Kabab")
print(item.category.name)

# ---------------------------------------------------------
# 14.  By using select and where, Find all desserts :
# ---------------------------------------------------------
des = Category.get(Category.name =="Dessert")
for food in Food.select().where(Food.category == des):
    print(food.name)

db.close()