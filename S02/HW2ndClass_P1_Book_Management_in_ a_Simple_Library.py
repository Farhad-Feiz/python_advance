from peewee import CharField, IntegerField,SqliteDatabase,Model,ForeignKeyField

db = SqliteDatabase("school.db")

class Student(Model):
    class Meta:
        database = db

    name = CharField()
    age  = IntegerField()

class Laptop(Model):
    class Meta:
        database = db

    brand = CharField()
    student = ForeignKeyField(Student, backref = 'laptops')

db.connect()

db.create_tables([Student , Laptop])

s = Student(name = "Ali", age = 15)
s.save()

Student.create(name = "Sara",age = 16)

Student.insert(name = "Farhad", age = 43).execute()
Student.insert(name = "Helen", age = 73).execute()
Student.insert(name = "Sogol", age = 34).execute()

l = Student.select()
for i in l:
    print(i.name)

a = Student.select().where(Student.name == "Sara")
for i in a:
    print(i.age)

"""
i = Student.select().where(Student.id == 1)
for i in i:
    print(i.name)

"""
# print(Student.select().count())

# for student in Student.select().where(Student.age == 15):
#     print(student.name)

"""

# دانش امزایه بالای ۱۵ اسمشون چاپ بشه
for student in Student.select().where(Student.age > 15):
    print(student.name)

for student in Student.select().where(Student.age < 16):
    print(student.name)

for student in Student.select().where(Student.name == "Ali" & Student.age == 15):
    print(student.name)

s1 = Student.get(Student.name == "Ali")
Laptop.create(brand = "ASUS", student = s1)

for lap in s1.laptops:
    print(lap.brand)

# for student in Student.select().where(Student.name == "Helen")
# Laptop.create(brand = "Sony", student = "Helen")

s2 = Student.get(Student.name == "Sara")
Laptop.create(brand = "Lenovo", student = s2)

for lap in s2.laptops:
    print(lap.brand)

s3 = Student.get(Student.name == "Helen")
Laptop.create(brand = "Dell", student = s3)

for lap in s3.laptops:
    print(lap.brand)

s4 = Student.get(Student.name == "Farhad")
Laptop.create(brand = "Toshiba", student = s4)

for lap in s4.laptops:
    print(lap.brand)

s5 = Student.get(Student.name == "Sogol")
Laptop.create(brand = "Toshiba", student = s5)

for lap in s5.laptops:
    print(lap.brand)

"""

# This code won't work because it makes a Query Set which is a list and ForeignKeyField doesn't accept a list!!!
# l = Student.select().where(Student.age > 15)--? [obj1, obj2]
# Laptop.create(brand = "Hewlet", student = l)
for i in l :
    Laptop.create(brand = "Hewlet", student = i)


# l2 = Student.get(Student.age > 15)
# Laptop.create(brand = "Hawal" , student = l2)

# for lap in l2.laptops:
#     print(lap.brand)

"""
h = Laptop.get(Laptop.brand == "Hawal")
# چرا این کد کار نمیکنه؟
# اگه ما بخوایم به افراد بالای ۱۵ سال به همه یه لپتاپ بدیم و بعدم اسماشون رو بخوایم چه کدی بزنیم؟
# h = Laptop.select().where(Laptop.brand == "Hewlet")
print(h.student.name)

# This code says all students above 15 gets a an IBM laptop (it proceeds one by one)
for st in Student.select().where(Student.age >15):
    Laptop.create(brand = "IBM",student = st)
# List of all students with an IBM laptop
for lap in Laptop.select().where(Laptop.brand == "IBM"):
    print(lap.student.name)

"""

# a1 = Student.get(Student.name == "Ali")
# Laptop.create(brand = "Macbook",student = a1)

# for lap in Laptop.select().where(Laptop.brand == "Hawal"):
#     print(lap.brand, "=>" lap.student.name)

"""
# علی را مستقیم پیدا میکنه
ali = Student.get((Student.name == "Ali") )

#  بصورت لیست در یک متغیر قرار میده !!! QuerySet!!!لپتاپهایی که مال علی هستند را پیدا میکنه
laptops = Laptop.select().where(Laptop.student == ali)
for lap in laptops:
    print(lap.brand)

# لپتاپهای برند Lenovo را پیدا میکنه
lap = Laptop.get(Laptop.brand == "Lenovo")

# اسم صاحبش را چاپ میکنه
print(lap.student.name)

# همه لپتاپای Toshiba را پیدا میکنه 
# صاحب هر کدام را جداگانه پیدا(واکشی) میکند
# نام آنها را چاپ میکند
for lap in Laptop.select().where(Laptop.brand == "Toshiba"):
    print(lap.brand, "=>", lap.student.name)

lap2 = Laptop.get(Laptop.brand == "Toshiba")
print(lap2.student.name)

# علی را پیدا میکند
a1 = Student.get(Student.name =="Ali")
# سن او را تغییر داده
a1.age = 18
# ذخیره میکند
a1.save() 

# سن سارا مستقیم آپدیت شده
Student.update(age =19).where(Student.name == "Sara").execute()

s2 = Student.get(Student.id == 2)
s2.delete_instance()

# لپتاپ های Lenovoپاک میشوند 
Laptop.delete().where(Laptop.brand == "Lenovo").execute()

# سن دانش آموزها از کم به زیاد مرتب میشوند
for st in Student.select().order_by(Student.age):
    print(st.name, st.age)
"""

# سن دانش آموزها از زیاد به کم مرتب میشوند
for st in Student.select().order_by(Student.age.desc()):
    print(st.name)

# نام لپتاپها به ترتیب حروف تلفبا مرتب میشن
for lap in Laptop.select().order_by(Laptop.brand):
    print(lap.brand)

db.close()
