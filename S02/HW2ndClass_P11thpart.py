from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField

db = SqliteDatabase("library.db")

class Author(Model):
    name = CharField()
    country = CharField()

    class Meta:
        database = db

class Book(Model):
    title = CharField()
    pages = IntegerField()
    author = ForeignKeyField(Author, backref='books')

    class Meta:
        database = db

db.connect()
db.create_tables([Author, Book])


# نویسنده‌ها
a1 = Author.create(name="Hemingway", country="USA")
a2 = Author.create(name="Kafka", country="Czech Republic")
a3 = Author.create(name="Shahriar", country="Iran")
# انتخاب نویسنده
selected_author = Author.get(Author.name == "Kafka")

# کتاب‌ها
Book.create(title="The Trial", pages=240, author=selected_author)
Book.create(title="Old Man and The Sea", pages=180, author=a1)
Book.create(title="Heydar Babaye Salam", pages=300, author=a3)

# چاپ همه کتاب‌ها
for b in Book.select():
    print(b.title)

# کتاب‌های بیش از ۲۰۰ صفحه
for b in Book.select().where(Book.pages > 200):
    print(b.title)

# تعداد نویسنده ها
print("تعداد نویسنده‌ها:", Author.select().count())

# مرحله ۱۳: گرفتن یک کتاب و چاپ نام نویسنده‌اش
book = Book.get(Book.title == "The Trial")
print("Book title:", book.title)
print("Author name:", book.author.name)

# مرحله ۱۴: پیدا کردن تمام کتاب‌های یک نویسنده خاص
author = Author.get(Author.name == "Kafka")
books = Book.select().where(Book.author == author)

for b in books:
    print(b.title)



db.close()