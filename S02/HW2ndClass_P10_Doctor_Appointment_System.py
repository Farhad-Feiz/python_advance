from peewee import CharField,IntegerField,SqliteDatabase,Model,ForeignKeyField,DateTimeField
from datetime import date

db = SqliteDatabase("clinic.db")

class Doctor(Model):
    class Meta:
        database = db

    name = CharField()
    specialty = CharField()

class Patient(Model):
    class Meta:
        database = db

    name            = CharField()
    national_code   = CharField()

class Appointment(Model):
    class Meta:
        database = db

    doctor  = ForeignKeyField(Doctor , backref= "appointments")
    patient = ForeignKeyField(Patient, backref= "appointments")
    date    = CharField()
    time    =CharField()

db.connect()

db.create_tables([Doctor , Patient , Appointment])
# -----------------------------
# 1. Insert sample data
# -----------------------------
d1 = Doctor.create(name="Dr. Ali", specialty="Heart")
d2 = Doctor.create(name="Dr. Sara", specialty="Eye")
d3 = Doctor.create(name="Dr. Reza", specialty="Neurology")

p1 = Patient.create(name="Amir", national_code="111")
p2 = Patient.create(name="Nima", national_code="222")
p3 = Patient.create(name="Maryam", national_code="333")
p4 = Patient.create(name="Sahar", national_code="444")
p5 = Patient.create(name="Farhad", national_code="555")

Appointment.create(doctor=d1, patient=p1, date="1403-01-01", time="09:00")
Appointment.create(doctor=d1, patient=p2, date="1403-01-01", time="10:00")
Appointment.create(doctor=d2, patient=p3, date="1403-01-02", time="11:00")
Appointment.create(doctor=d3, patient=p4, date="1403-01-03", time="12:00")
Appointment.create(doctor=d3, patient=p5, date="1403-01-03", time="13:00")
Appointment.create(doctor=d2, patient=p1, date="1403-01-04", time="09:00")

# ------------------------------------
# 2. Show doctor appointments by name:
# ------------------------------------
def show_doctor_appointment(name):
    try:
        doctor = Doctor.get(Doctor.name == name)
    except Doctor.DoesNotExist:
        print(f"Doctor Not Found!!!")
        return

    
    apps = Appointment.select().where(Appointment.doctor == doctor).order_by(Appointment.date,Appointment.time)
    print(f"n\Appointments for {doctor.name}")

    for a in apps:
        print(f"{a.date},   |   ,{a.time},  |   Patient : {a.patient.name}")

def show_patient_appointment(code):
    try:
        patient = Patient.get(Patient.national_code == code)
    except Patient.DoesNotExist:
        print(f"\nPatients Not Found!!!")
        return

    apps = Appointment.select().where(Appointment.patient == patient).order_by(Appointment.date)
    for a in apps:
        print(f"\n{a.date}, |   ,{a.time},  |   Doctor : {a.doctor.name},   |   {a.doctor.specialty}")

# -----------------------------------------------------------------
# 4. Create appointment (check doctor conflict + patient conflict) :
# -----------------------------------------------------------------
def create_appointment(doctor_name, patient_code,date,time):
    try:
        doctor = Doctor.get(Doctor.name == doctor_name)
        patient = Patient.get(Patient.national_code == patient_code)
    except:
        print("Doctor or patient not found !!!")

    conflict = Appointment.select().where(Appointment.doctor==doctor,Appointment.date == date, Appointment.time == time)
    if conflict.exists():
        print("Doctor already has an appointment at this time!!! ")
        return

    conflict2 = Appointment.select().where(Appointment.date == date,Appointment.time == time)
    if conflict2.exists():
        print("PAtient has an appoinment at this time!!! ")
        return
    Appointment.create(doctor = doctor, patient = patient,date=date , time=time)
# -----------------------------
# 5. Delete appointment
# -----------------------------
def delete_appointment(patient_name,date,time):
    try:
        patient = Patient.get(Patient.name == patient_name)
    except Patient.DoesNotExist:
        print("Patient Not Found...!!! ")
    try:
        app = Appointment.get((Appointment.patient == patient_name)&(Appointment.date==date)&(Appointment.time==time))
        app.delete_instance()
        print("Appointment is deleted!!!")
    except Appointment.DoesNotExist:
        print("Appointmnet Not Found!!!")    
# --------------------------------
# 6. Change appointment time/date :
# --------------------------------
def change_appointment(patient_name ,old_date, old_time, new_date, new_time):
    try: 
        patient = Patient.get(Patient.name == patient_name)
        app     = Appointment.get((Appointment.patient == patient_name)&(Appointment.date == old_date)&(Appointment.time == old_time))

    except:
        print("Appointment was not found!!!")
        return

    # Check Doctor Conflict
    conflict = Appointment.select().where(Appointment.doctor == app.doctor , Appointment.date == new_date , Appointment.time == new_time)

    if conflict.exists():
        print("Doctor has already an appointment")
        return

    app.date = new_date
    app.time = new_time
    app.save()
    print("\nAppointment updated")

# ------------------------------------
# 7. Doctor timetable in date range :
# ------------------------------------
def doctor_timetable(name , start_date, end_date):
    try:
        doctor = Doctor.get(Doctor.name == name)
    except:
        print("Doctor not found!!!")
        return
    print(f"Time table for : {doctor.name}, From {start_date}, To , {end_date}")
    apps = Appointment.select().where((Appointment.doctor==doctor) & (Appointment.date.between(start_date,end_date))).order_by(Appointment.date,Appointment.time)
    if apps:
        for a in apps:
            print(f"{a.date},   |   ,   {a.time},   |   ,Patient : {a.patient.name}")
            
# -----------------------------
# 8. Doctors with appointments today
# -----------------------------         
def doctors_today(today):
    print("\nDoctors with appointments today:")
    apps = Appointment.select().where(Appointment.date == today)

    if not apps:
        print("No appointments today.")
        return

    for a in apps:
        print(f"{a.doctor.name},  |   ,{a.doctor.specialty},   |   ,Patient : {a.patient.name},     |   {a.time}")

# -----------------------------
# 10. Doctor with most appointments
# -----------------------------
def doctor_most_appointments():
    max_doc = None
    max_count = 0

    for d in Doctor.select():
        count = d.appointments.count()
        if count > max_count:
            max_count = count
            max_doc = d

    print(f"{max_doc.name},    |   ,   {max_count}")

db.close()
# -----------------------------
# 11. Patient conflict check already included in create_appointment()
# -----------------------------

# -----------------------------
# Example calls
# -----------------------------
show_doctor_appointment("Dr. Ali")
show_patient_appointment("111")
create_appointment("Dr. Ali", "555", "1403-01-01", "09:00")
delete_appointment("Amir", "1403-01-01", "09:00")
change_appointment("Nima", "1403-01-01", "10:00", "1403-01-01", "11:00")
doctor_timetable("Dr. Reza", "1403-01-01", "1403-01-10")
doctors_today("1403-01-03")
doctor_most_appointments()
doctor_most_appointments()