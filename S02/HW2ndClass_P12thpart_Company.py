from peewee import CharField, ForeignKeyField, IntegerField, Model, SqliteDatabase
# --------------------------------------
# 1.  Database constructiom
# --------------------------------------
db = SqliteDatabase("comapny.db")


# --------------------------------------
# 2.  Department Class
# --------------------------------------

class Department(Model):

    name = CharField()

    class Meta:
        database = db
# --------------------------------------
# 3.   Employee Class   &   4.   ForeignKeyField
# --------------------------------------

class Employee(Model):

    name = CharField()
    salary = IntegerField()
    department = ForeignKeyField(Department, backref="employees")

    class Meta:
            database = db



db.connect()
# --------------------------------------
# 5.   Create Tables :
# --------------------------------------

db.create_tables([Department, Employee])

# --------------------------------------
# 6.   Create Departments :
# --------------------------------------

d1 = Department.create(name="IT")

d2 = Department.create(name="Finance")

d3 = Department.create(name="Sales")


# --------------------------------------
# 7.   Find The IT Department :
# --------------------------------------
it_dept = Department.get(Department.name == "IT")

# --------------------------------------
# 8.   Create an Employee IT :
# --------------------------------------

Employee.create(name="Rostam", salary=20000, department=it_dept)

# --------------------------------------
# 9.   Create an Employee IT :
# --------------------------------------
Employee.create(name="Jade", salary=12000, department=d2)

Employee.create(name="Sara", salary=18000, department=d3)


# --------------------------------------
# 10.   Print All Employees :
# --------------------------------------
print("\n All Employees")
for emp in Employee.select():
    print(emp.name)

# --------------------------------------
# 11.   Print Employees Earning salary more than 15000 :
# --------------------------------------
print("\n Employees with salary > 15000")
for emp in Employee.select().where(Employee.salary > 15000):
    print(emp.name)

# --------------------------------------
# 12.  Count how many departments exist :
# --------------------------------------

print(Department.select().count())

# ------------------------------------------------------------
# 13.   Read an employee and print their department name :
# ------------------------------------------------------------

emp = Employee.get(Employee.name == "Sara")

print("\n Sara works in the following department:") 
print(emp.department.name)

# ----------------------------------------
# 14.   Print employees who work in Sales:
# ----------------------------------------

dep = Department.get(Department.name == "Sales")

print("\n People who work in sales department : ")
for emp in Employee.select().where(Employee.department == dep):
    print(emp.name)


db.close()