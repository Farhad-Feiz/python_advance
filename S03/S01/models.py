from peewee import BooleanField, CharField, IntegerField, Model, SqliteDatabase,ForeignKeyField


db = SqliteDatabase("library2.db")

class Base(Model):
    class Meta:
        database = db

class Author(Base):
    
    name = CharField()
    country = CharField()

class Book(Base):
    title = CharField()
    pages = IntegerField()
    author= ForeignKeyField(Author , backref="books")

with db.connection_context():
    db.create_tables([Author , Book])


# Library.create(title="Gone with the wind", author="George Orwell", year=1836, available=True)


# Library.create(title="Great Expectations", author="Charls Dickens", year=1845, available=True)


# Library.create(title="Long Leg Dady", author="annanymous", year=1800, available=False)


# Library.create(title="Klimanjaro", author="denzel washington", year=1997, available=True)


# Library.create(title="Around the World", author="Danny O'Brien", year=2006, available=True)

# l = Library.select().where(Library.available == True)
# for i in l:
#     print(i.title)

# l = Library.get(Library.title == "Long Leg Dady")
# l.available = True
# l.save()





# db.close()

# class Person:
#     def __init__(self,n,f,a):
#         self.name = n
#         self.family = f
#         self.age = a

#     def speak(self):
#         return f"Hi, I speak English"


#     def say_hello(self):
#         ...
    
# # P1 = Person("Farhad","Feiz",44)
# # p2 = Person("Amir","Nakhayi", 38)


# class Student(Person):

#     def __init__(self, n, f, a, s):
#         super().__init__(n, f, a)

#         self.scores = s

#     def study(self):
#         return f" Hi ,I'm {self.name} and I'm studying"
    
# class Teacher(Person):  
#     def teach(self):
#         return  f"Hi, I'm {self.name}and I teach 4 days a  week"
# class Manager(Person):
#     def mangage(self):
#         return f"Hi, I'm {self.name},  I'm the new manager!"

# m = Manager("Rostam","Feiz",44)
# s1 = Student("Ali","Tahouri", 36, 80)


# print(m.speak() ,m.mangage())
# print(Manager.mro())
# print(s1.study())


# d = far{}
# while True:
#     user_name= input ("Please enter your username : ")

#     if user_name not in d:
#         password = input ("Please enter your password : ")
#         d[user_name]=password

