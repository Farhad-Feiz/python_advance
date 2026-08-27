from peewee import CharField,IntegerField,Model,SqliteDatabase,ForeignKeyField

db = SqliteDatabase("support.db")

# --------------------------------------
#        Creat User Class
# --------------------------------------
class User(Model):
    class Meta:
        database = db
    name = CharField()

class Ticket(Model):
    class Meta:
        database = db

    title   = CharField()
    message = CharField()
    status  = CharField(default="open") #   Open/Close
    user    = ForeignKeyField(User , backref= "tickets")

# -----------------------------
# Create tables
# -----------------------------
db.connect()
db.create_tables([User, Ticket])


# -----------------------------
# 1. Insert sample users & tickets
# -----------------------------
u1 = User.create(name="Ali")
u2 = User.create(name="Sara")
u3 = User.create(name="Reza")

Ticket.create(title="Login Issue", message="Cannot login", status="open", user=u1)
Ticket.create(title="Payment Error", message="Card declined", status="closed", user=u1)
Ticket.create(title="Bug Report", message="App crashes", status="open", user=u2)
Ticket.create(title="Feature Request", message="Add dark mode", status="open", user=u3)
Ticket.create(title="Slow Website", message="Very slow", status="open", user=u3)

# -----------------------------
# 2. Show all open tickets
# -----------------------------
print("\n--- Open Tickets ---")
open_tickets = Ticket.select().where(Ticket.status == "open")
for t in open_tickets:
    print(f"{t.id} |   {t.title} |   {t.user.name}")

# -----------------------------
# 3. Close a specific ticket
# -----------------------------
print("\n--- Closing Ticket with title='Bug Report' ---")
t = Ticket.get(Ticket.title == "Bug Report")
t.status = "closed"
t.save()

# -----------------------------
# 4. Show tickets of a specific user
# -----------------------------
print("\n--- Tickets of user Reza ---")
user_tickets = Ticket.select().where(Ticket.user == u3)
for t in user_tickets:
    print(f"{t.title} | {t.status}")

# -----------------------------
# 5. Find users with more than 3 open tickets
# -----------------------------
print("\n--- Users with more than 3 open tickets ---")

for user in User.select():
    open_count = Ticket.select().where((Ticket.user == user)&(Ticket.status=="open")).count()
    if open_count > 3 :
        print(f"{user.name} , {open_count}")

db.close()
