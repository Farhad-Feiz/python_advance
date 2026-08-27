"""
# Person --> class
# attribute / property ---> name / family / age / ....
# behavior ---> speak / say_hello /  ....
# morteza - abbaszadeh --> object

# Car  --> class
# attribute / property --> year / name  / color 
# behavior ---> ....
# pride --> object


# product  --> class
# attribute / property --> name / tozihat / 
# behavior 
# jorab  --> object

# str --> class
# attribute / property --> '' / ""
# behavior --> upper() / lower() / isupper() / replace() 
# 'ali'  --> object

# int --> class
# attribute / property 
# behavior
# 2 --> object
"""
"""
# 
class Person:
    
    #  attribute
    # dunder method - magic function
    def __init__(self , n, f , a ):
        self.name = n
        self.family = f 
        self.age = a

        
    # behavior
    def speak(self):
        ...
        
    def say_hello(self):
        ...
         
p1 = Person( 'reza','rezaii',20 )       
# Person.__init__('p1' , 'reza','rezaii',20 ) 
p2 = Person( 'jasem','jasemi', 22 )       
# Person.__init__('p2' , 'jasem','jasemi',22 ) 

"""
"""
class Person:
        
    def __init__(self , n, f , a ):
        self.name = n
        self.family = f 
        self.age = a
        
    # behavior
    def speak(self):
        return 'Hi its person'
        
    def say_hello(self):
        ...


class Student(Person):
    
    def __init__(self , n, f , a , s ):
        super().__init__(n,f,a)
       # Person.__init__(self , n, f , a)
        
        
        self.scores = s
        
    def study(self):
        return f'Hi, Im {self.name} and im studing'
    
# is a 
class Teacher(Person) : 

    def teach(self):
        return f'Hi, Im {self.name} and im teaching'
    
# is a
class Manager(Person):

    def manage(self):
        return f'Hi, Im {self.name} and im manage'
    
m = Manager('reza' ,'jasemian' ,20)
print(Manager.mro())
"""

# login - instagram 
"""
d = {}
while True :
    username = input('username: ')
 
    if username not in d:
        password = input('password: ')
        d[username] = password
"""

"""f = open('a.txt' , 'w')

with open('a.txt' , 'w') as f :
    pass
    
"""


# data-base
# sql - sqlite - mysql - postgressql - nosql - redis

# ORM --> Object Relation Map

"""
class --> table 
atrribute --> column
object --> row
"""
'''
class User:
    name   = 
    family = 
    age    = 
    code   =
User(name='reza' , family='jasemi' , age=20 , code=87628712)
'''
"""
from peewee import SqliteDatabase ,CharField,IntegerField , Model

# type - address
db = SqliteDatabase('example.db')

class User(Model):
    class Meta :
        database = db 
        
    name   = CharField()
    family = CharField()
    age    = IntegerField()
    code   = IntegerField()

db.connect()

db.create_tables([User])

# crud --> create / read . update . delete 


# add

User.create(name='kazem' , age =23 ,family = 'ghanbari' , code =4325)
User.create(name='jasem' , age =25 ,family = 'jabari' , code =89756723421)
User.create(name='lazem' , age =0 ,family = 'janboii' , code =2)


# delete
# find
k = User.get( User.id == 'lazem')
k.delete_instance()

# update 
# find 
k = User.get(User.name == 'reza')
k.family = 'hassani'
k.save()

# get / select
a = User.select() # list
for i in a:
    print(i.code)
  
a = User.select().where(User.name == 'reza') # list
for i in a:
    print(i.code)
db.close()

"""

"""

from peewee import SqliteDatabase , CharField , IntegerField , BooleanField , Model

db = SqliteDatabase('example.db')

class Book(Model) :
    class Meta :
        database = db
    
    Title = CharField(unique=True )
    Author = CharField()
    Year = IntegerField()
    Available = BooleanField(default=True)


db.connect()

db.create_tables([Book])

try : 
    
    Book.create(Title = 'The Little Prince' , Author = 'Antoni de' , Year = 1990 )
    Book.create(Title = 'Charlote Web' , Author = 'E.B. White' , Year = 2000 , Available = False)
    Book.create(Title = 'Wonder' , Author = 'Palacio' , Year = 1970 , Available = False)
    Book.create(Title = 'The Old Man' , Author = 'Hemingtone' , Year = 1980 , Available = True)
    Book.create(Title = 'Animal Farm' , Author = 'Orwell' , Year = 2005 , Available = True)
except :
    print('Error')


a = Book.select().where(Book.Title == 'Wonder') # list
for i in a :
    i.delete_instance()


b = Book.get(Book.Title == 'Wonder')
b.Year = 1977
b.save()

db.close()

"""

from peewee import SqliteDatabase , CharField , IntegerField , BooleanField , Model,ForeignKeyField
db = SqliteDatabase('shop.db')


class Base (Model):
    class Meta : 
        database = db
    


class Foroshande(Base):
    name   =  CharField()
    family = CharField()
    code   = CharField(unique = True,primary_key=True)
    
class Kharidar(Base) : 
    name   =  CharField()
    family = CharField()
    code   = CharField(unique = True,primary_key=True)
    
class Kala (Base): 
    name = CharField(primary_key=True)
    code = CharField(unique = True)
    gheymat = IntegerField()
    
    
class Forosh(Base):
    kharidar__   = ForeignKeyField(Kharidar)
    foroshande__ = ForeignKeyField(Foroshande)
    kala__       = ForeignKeyField(Kala)
    ghemat = IntegerField()

db.connect()

db.create_tables([Forosh,Foroshande,Kharidar,Kala])
for i in range(5):
    Foroshande.create(name=f'jasem_{i}', code=23423*i ,family='kazemi' )
    Kharidar.create(name=f'sara_{i}' , code=453*i , family='jabari')
    Kala.create(name=f'shokolat_{i}' , code=345345*i , gheymat=1000*i*2.2)

k = Kala.get(Kala.name=='shokolat_1')
f = Foroshande.get(Foroshande.name=='jasem_1' )
kh = Kharidar.get(Kharidar.name=='sara_1') 
Forosh.create(ghemat=102992 ,kharidar__ =kh ,foroshande__ =f, kala__ =k   )




db.close()