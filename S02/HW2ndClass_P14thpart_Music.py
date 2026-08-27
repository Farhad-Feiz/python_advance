from peewee import SqliteDatabase,CharField,IntegerField,Model,ForeignKeyField

# --------------------------------------
# 1.  Database constructiom
# --------------------------------------

db =SqliteDatabase("msuic.db")

# --------------------------------------
# 2.  Create Artist model :
# --------------------------------------

class Artist(Model):
    class Meta:
        database = db

    name = CharField()
# --------------------------------------
# 3.    Create Song Model : :
# --------------------------------------
class Song(Model):
    class Meta:
        database = db

    title = CharField()
    duration = IntegerField()
# --------------------------------------
# 4.    ForeignKeyField : :
# --------------------------------------
    artist = ForeignKeyField(Artist , backref= "songs")

# --------------------------------------
# 5.    Create  two Tables: :
# --------------------------------------
db.connect()

db.create_tables([Artist , Song])
# --------------------------------------
# 6.   Create  three Singers: :
# --------------------------------------
a1 = Artist.create(name = "Leonard Cohen")
a2 = Artist.create(name = "Bryan Adams")
a3 = Artist.create(name = "Michael Bolton")
a5 = Artist.create(name = "Elton John")
a6 = Artist.create(name = "Whitney Houston")

# --------------------------------------
# 7.   Find one singer by get method: :
# --------------------------------------
s1 = Artist.get(Artist.name == "Elton John" )

# --------------------------------------
# 8.   Crean a New Song: :
# --------------------------------------

Song.create(title = "Sacrifice" , duration = 245 , artist = a5)

# --------------------------------------
# 9.   Create two more Songs : :
# --------------------------------------
Song.create(title = "Everybody Knows" , duration = 370 , artist = a1)
Song.create(title = "Everything I Do" , duration = 380 , artist = a2)
Song.create(title = "Said I Loved You" , duration = 303 , artist = a3)
Song.create(title = "I Will Always Love You" , duration = 303 , artist = a6)
# --------------------------------------
# 10.   Print All Songs : :
# --------------------------------------

for s in Song.select():
    print(s.title)
# --------------------------------------
# 11.   Find songs longer than 200s : 
# --------------------------------------
for s in Song.select().where(Song.duration >= 300):
    print(s.title , s.duration)

# --------------------------------------
# 12.   Number of singers by count method :
# --------------------------------------

print(Artist.select().count())
# ----------------------------------------------
# 13.   Call a Song by get and find its singer :
# ----------------------------------------------

s1 = Song.get(Song.title == "Sacrifice")
print(s1.artist.name)

# ----------------------------------------------
# 14.   Call a Song by get and find its singer :
# ----------------------------------------------
singer = Artist.get(Artist.name =="Leonard Cohen")

for song in Song.select().where(Song.artist == singer):
    print(song.title)


db.close()