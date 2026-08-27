from peewee import SqliteDatabase,CharField,IntegerField,BooleanField,Model,ForeignKeyField,DateTimeField
from datetime import datetime,timedelta

# --------------------------------------
#        Database constructiom
# --------------------------------------
db = SqliteDatabase("comment.db")


# --------------------------------------
#         Create Artist User :
# --------------------------------------
class User(Model):
    class Meta:
        database = db 

    name = CharField()

# --------------------------------------
#        Create Comment Model : 
# --------------------------------------
class Comment(Model):
    class Meta:
        database = db

    text = CharField()
    created_at = DateTimeField()
# --------------------------------------
#           ForeignKeyField :
# --------------------------------------
    user = ForeignKeyField(User , backref=  "comments")


db.connect()
# --------------------------------------
#        Create  two Tables : 
# --------------------------------------
db.create_tables([User , Comment])

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
# 1.   Create  Some Comments :
# --------------------------------------
Comment.create(user = u1 , text = "It's Gr8!" , created_at = datetime(2024 , 5 , 10) )
Comment.create(user = u1 , text = "Nice article" , created_at = datetime.now())
Comment.create(user = u2 , text = "Good News!" , created_at = datetime(2024 , 5 ,8))
Comment.create(user = u2 , text = "Good News!" , created_at = datetime(2024 , 5 ,12))
Comment.create(user = u3 , text = "Good News!" , created_at = datetime(2024 , 5 ,17))
Comment.create(user = u3 , text = "I'm pretty  sure she calls soon!" , created_at = datetime(2024 , 5 ,24))
Comment.create(user = u3 , text = "She loves you" , created_at = datetime(2024 , 5 ,28))
Comment.create(user = u4 , text = "She loves youTake her out" , created_at = datetime(2024 , 5 ,29))
Comment.create(user = u4 , text = "She feels lonely" , created_at = datetime(2024 , 5 ,30))
Comment.create(user = u5 , text = "She misses you" , created_at = datetime(2024 , 6 ,30))
Comment.create(user = u5 , text = "It is what it is" , created_at = datetime(2024 , 8 ,25))
Comment.create(user = u5 , text = "Loves you so much!" , created_at = datetime(2024 , 9 ,25))

# --------------------------------------
# 2.   Print a Specific User Comments :
# --------------------------------------
u1 = User.get(User.name == "Rostam")
print("\nRostam wrote the following comments :")
for com in Comment.select().where(Comment.user == u1):
    print(com.text)

# ---------------------------------------------
# 3.   Delete Comments Older Than (2004,5,17) :
# ---------------------------------------------
limit_date = datetime(2024 , 5 , 17)
Comment.delete().where(Comment.created_at < limit_date).execute()

# ---------------------------------------------
# 4.   Print All Comments With Their Names :
# ---------------------------------------------
print("\n All Comments :")
for c in Comment:
    print(c.user.name,"-----",c.text)

# ----------------------------------------------------------
# 5.   Delete a Specific User in a Specified Time Interval :
# ----------------------------------------------------------
start = datetime(2024 , 5 ,17)
end   = datetime(2024 , 5 ,25)

helen = User.get(User.name == "Helen" )
for c in Comment.select().where(Comment.user== helen & Comment.created_at.between(start,end)):
    c.delete_instance()

# ----------------------------------------------------------
# 6.   Searching Comments Containg a specific "Word" :
# ----------------------------------------------------------
for c in Comment.select().where(Comment.text.contains("love")):
    print(c.user,"------",c.text)

# ----------------------------------------------------------
# 7.   All Recorded Comments" :
# ----------------------------------------------------------
print(Comment.select().count())
# ----------------------------------------------------------
# 8.   User List with No Comments :
# ----------------------------------------------------------
print("\n Users with no comments :")
for user in User.select():
    if (user.comments.count() == 0):
        print(user.name)

db.close()