from peewee import CharField, ForeignKeyField, IntegerField, Model, SqliteDatabase

# --------------------------------------
# 1.  Database constructiom
# --------------------------------------
db = SqliteDatabase("Scores.db")

# --------------------------------------
# 2.  Create Student model :
# --------------------------------------

class Student(Model):
    class Meta:
        database=db

    name = CharField()
    student_code = IntegerField()
# --------------------------------------
# 2.  Create Grade model :
# --------------------------------------

class Grade(Model):
    class Meta:
        database=db

    course_name = CharField()
    score = IntegerField()
# --------------------------------------
# 4.    ForeignKeyField : :
# --------------------------------------

    student = ForeignKeyField(Student, backref="grades")

db.connect()
# --------------------------------------
# 5.    Create  two Tables: :
# --------------------------------------

db.create_tables([Student,Grade])

# --------------------------------------
# 6.   Create  Five Students: :
# --------------------------------------

"""
Student.create(name="Ali", student_code="A01")
Student.create(name="Abbas", student_code="A02")
Student.create(name="Akbar", student_code="A03")
Student.create(name="Asghar", student_code="A04")
Student.create(name="Bahram", student_code="A06")
Student.create(name="Rostam", student_code="A07")
"""
# Student.update(student_code="A20").where(Student.name=="Asghar").execute()

# --------------------------------------
# 7.   Find Five Student by "get" method: :
# --------------------------------------

ali = Student.get(Student.name == "Ali")
bahram = Student.get(Student.name == "Bahram")
abbas = Student.get(Student.name == "Abbas")
akbar = Student.get(Student.name == "Akbar")
asghar = Student.get(Student.name == "Asghar")
rostam = Student.get(Student.name == "Rostam")

# --------------------------------------
# 8.   Crean New Songs: :
# --------------------------------------
Grade.create(course_name = "Geography" , score = 18, student=ali)
Grade.create(course_name = "Math" , score = 19, student=ali)
Grade.create(course_name = "Chemistry" , score = 17, student=ali)
Grade.create(course_name = "Science" , score = 18, student=ali)
Grade.create(course_name = "Fine Arts" , score = 15, student=ali)
Grade.create(course_name = "Language" , score = 20, student=ali)
Grade.create(course_name = "Economy" , score = 19, student=ali)
Grade.create(course_name = "Biology" , score = 18, student=ali)
Grade.create(course_name = "Literature" , score = 19, student=ali)
Grade.create(course_name = "History" , score = 16, student=ali)

# print(ali.id, ali.name)


# for s in Student.select():
#     print(s.id, s.name)


# Grade.create(course_name = "Geography" , score = 15, student=abbas)
# Grade.create(course_name = "Math" , score = 14, student=abbas)
# Grade.create(course_name = "Chemistry" , score = 10, student=abbas)
# Grade.create(course_name = "Science" , score = 19, student=abbas)
# Grade.create(course_name = "Fine Arts" , score = 11, student=abbas)
# Grade.create(course_name = "Language" , score = 2, student=abbas)
# Grade.create(course_name = "Economy" , score = 5, student=abbas)
# Grade.create(course_name = "Biology" , score = 14, student=abbas)
# Grade.create(course_name = "Literature" , score = 12, student=abbas)
# Grade.create(course_name = "History" , score = 0, student=abbas)



# Grade.create(course_name = "Geography" , score = 19, student=akbar)
# Grade.create(course_name = "Math" , score = 19, student=akbar)
# Grade.create(course_name = "Chemistry" , score = 18, student=akbar)
# Grade.create(course_name = "Science" , score = 18, student=akbar)
# Grade.create(course_name = "Fine Arts" , score = 20, student=akbar)
# Grade.create(course_name = "Language" , score = 20, student=akbar)
# Grade.create(course_name = "Economy" , score = 19, student=akbar)
# Grade.create(course_name = "Biology" , score = 20, student=akbar)
# Grade.create(course_name = "Literature" , score = 19, student=akbar)
# Grade.create(course_name = "History" , score = 20, student=akbar)



# Grade.create(course_name = "Geography" , score = 18, student=asghar)
# Grade.create(course_name = "Math" , score = 15, student=asghar)
# Grade.create(course_name = "Chemistry" , score = 11, student=asghar)
# Grade.create(course_name = "Science" , score = 13, student=asghar)
# Grade.create(course_name = "Fine Arts" , score = 15, student=asghar)
# Grade.create(course_name = "Language" , score = 20, student=asghar)
# Grade.create(course_name = "Economy" , score = 14, student=asghar)
# Grade.create(course_name = "Biology" , score = 16, student=asghar)
# Grade.create(course_name = "Literature" , score = 13, student=asghar)
# Grade.create(course_name = "History" , score = 16, student=asghar)

# ------------------------------------------------------------------------------------------------------------
#In the following code "bahram" was typed ,hence student_id column was printed as bahram instead of a number
# ------------------------------------------------------------------------------------------------------------
 
# Grade.create(course_name = "Geography" , score = 18, student="bahram")
# Grade.create(course_name = "Math" , score = 19, student="bahram")
# Grade.create(course_name = "Chemistry" , score = 17, student="bahram")
# Grade.create(course_name = "Science" , score = 18, student="bahram")
# Grade.create(course_name = "Fine Arts" , score = 15, student="bahram")
# Grade.create(course_name = "Language" , score = 20, student="bahram")
# Grade.create(course_name = "Economy" , score = 19, student="bahram")
# Grade.create(course_name = "Biology" , score = 18, student="bahram")
# Grade.create(course_name = "Literature" , score = 19, student="bahram")
# Grade.create(course_name = "History" , score = 16, student="bahram")



# ------------------------------------------------------------------------------------------------------------
#..............The following code erases all bahram's scores ----"bahram"
# ------------------------------------------------------------------------------------------------------------

# Grade.delete().where(Grade.student == "bahram").execute()


# ------------------------------------------------------------------------------------------------------------
#.........Recreate bahram's scores this time student = bahram ----NOT----"bahram"
# ------------------------------------------------------------------------------------------------------------

# Grade.create(course_name = "Geography" , score = 19, student=bahram)
# Grade.create(course_name = "Math" , score = 19, student=bahram)
# Grade.create(course_name = "Chemistry" , score = 19, student=bahram)
# Grade.create(course_name = "Science" , score = 17, student=bahram)
# Grade.create(course_name = "Fine Arts" , score = 18, student=bahram)
# Grade.create(course_name = "Language" , score = 20, student=bahram)
# Grade.create(course_name = "Economy" , score = 18, student=bahram)
# Grade.create(course_name = "Biology" , score = 19, student=bahram)
# Grade.create(course_name = "Literature" , score = 19, student=bahram)
# Grade.create(course_name = "History" , score = 19, student=bahram)

# Grade.delete().where(Grade.id==41).execute()


# ------------------------------------------------------------------------------------------------------------
#..........................................Highest & Lowest Score.............................................
# ------------------------------------------------------------------------------------------------------------
grades = list(rostam.grades)

if grades:
    highest = max(grades, key=lambda g: g.score)
    lowest = min(grades, key= lambda g: g.score)
    print("Highest :", highest.course_name,  highest.score)
    print("Lowest : ",lowest.course_name, lowest.score)

else:
    print("Rostam has no grades")

grades = list(bahram.grades)
if grades:
    highest = max(grades, key=lambda g: g.score)
    lowest = min(grades, key= lambda g: g.score)
    print("Highest :", highest.course_name,  highest.score)
    print("Lowest : ",lowest.course_name, lowest.score)

else:
    print("Bahram has no grades")


# ------------------------------------------------------------------------------------------------------------
#............................................UPDATE Specific Score...........................................
# ------------------------------------------------------------------------------------------------------------
"""
grade = Grade.get((Grade.student == bahram) & (Grade.course_name == "Math"))
grade.score = 11
grade.save()

grade = Grade.get((Grade.student == asghar) & (Grade.course_name == "Math"))
grade.score = 9
grade.save()

grade = Grade.get((Grade.student== ali) & (Grade.course_name == "History"))
grade.score = 5
grade.save()

grade = Grade.get((Grade.student == akbar) & (Grade.course_name == "History"))
grade.score = 5
grade.save

Grade.update(score=12).where(Grade.id==48).execute()
Grade.update(score=8).where(Grade.id==43).execute()
Grade.update(score= 6 ).where(Grade.id == 4).execute()
Grade.update(score=5).where(Grade.id==11).execute()
Grade.update(score=4).where(Grade.id==23).execute()
"""
# ------------------------------------------------------------------------------------------------------------
#............................................Delete Specific Score...........................................
# ------------------------------------------------------------------------------------------------------------

"""
grade = Grade.get((Grade.student==ali) & (Grade.course_name=="Biology"))
grade.delete_instance()

grade = Grade.get((Grade.student==akbar) & (Grade.course_name=="Biology"))
grade.delete_instance()

grade = Grade.get((Grade.student==asghar) & (Grade.course_name == "Biology"))
grade.delete_instance()

Grade.delete().where(Grade.id==32).execute()
Grade.delete().where(Grade.id==33).execute()
Grade.delete().where(Grade.id==30).execute()
"""
# ------------------------------------------------------------------------------------------------------------
#.................................................Passed Score................................................
# ------------------------------------------------------------------------------------------------------------
course = "Math"
pass_score = 10

passed_grades = Grade.select().where((Grade.score>= pass_score) & (Grade.course_name=="Math"))
students = [g.student for g in passed_grades]
print("Students who passed ", course," : ")
for s in students:
    print(s.name , s.student_code)

"""
print("--------------Ali's Grades-------------- ")
for g in ali.grades:
    print(g.course_name, g.score)

grades = ali.grades
total = sum(g.score for g in grades)
count=len(grades)
average= total / count
print("Ali's average is : ",average)




print("--------------Abbas's Grades-------------- ")
for g in abbas.grades:
    print(g.course_name, g.score)

grades = abbas.grades
total = sum(g.score for g in grades)
count=len(grades)
average= total / count
print("Abbas's average is : ",average)




print("--------------Akbar's Grades-------------- ")
for g in abbas.grades:
    print(g.course_name, g.score)

grades = akbar.grades
total = sum(g.score for g in grades)
count=len(grades)
average= total / count
print("Akbar's average is : ",average)


print("--------------Asghar's Grades-------------- ")
for g in abbas.grades:
    print(g.course_name, g.score)

grades = asghar.grades
total = sum(g.score for g in grades)
count = len(grades)
average = total/count

print("Asghar's average is : ",average)

print("--------------Bahram's Grades-------------- ")
for g in bahram.grades:
    print(g.course_name, g.score)
# grades = bahram.grades
total = sum(g.score for g in bahram.grades)
count = len(bahram.grades)
average = total/count
print("Bahram's average is : ",average)

# print("--------------Abbas's Grades-------------- ")
# for g in abbas.grades:
#     print(g.course_name, g.score)

# print("--------------Abbas's Grades-------------- ")
# for g in abbas.grades:
#     print(g.course_name, g.score)


"""
# print(Student._meta.fields)

db.close()