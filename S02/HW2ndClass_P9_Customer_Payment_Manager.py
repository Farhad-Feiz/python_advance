from peewee import CharField, DateTimeField, ForeignKeyField, IntegerField, Model, SqliteDatabase




db = SqliteDatabase("payment")

# --------------------------------------
#        Creat User Class
# --------------------------------------
class BaseModel(Model):
    class Meta:
        database = db

class Customer(BaseModel):
    name = CharField()

class Payment(BaseModel):
    amount = IntegerField()
    date = DateTimeField()
    customer = ForeignKeyField(Customer, backref="payments")

# -----------------------------
# Create tables
# -----------------------------

db.connect()
db.create_tables([Customer, Payment])

c1 = Customer.create(name="Ali")
c2 = Customer.create(name="Sara")
c3 = Customer.create(name="Reza")

Payment.create(amount=50000, date="1403-01-01", customer=c1)
Payment.create(amount=70000, date="1403-01-05", customer=c1)
Payment.create(amount=80000, date="1403-02-10", customer=c2)
Payment.create(amount=40000, date="1403-03-12", customer=c3)
Payment.create(amount=30000, date="1403-03-20", customer=c3)
Payment.create(amount=20000, date="1403-03-25", customer=c3)

# -------------------------------------------------------
# 2. Total payments of a specific customer (example: Ali)
# -------------------------------------------------------
toatal_ali=sum(t.amount for t in Payment.select().where(Payment.customer == c1))
print("Ali", toatal_ali)

# toatal_ali = Payment.select().where(Payment.customer == c1) + sum((t.amount for t in toatal_ali))

for p in c2.payments:

    pass

print("Ali", toatal_ali)

# --------------------------------------
# 3. Show customers who paid more than X
# --------------------------------------

print("\n--- Customers who paid more than 100000 ---")

X = 100000

for customer in Customer.select():
    total = sum(p.amount for p in customer.payments)

    if total > X:
        print(f"{customer.name},------->,{total}")
# ------------------------------------------
# 4. Show total payments for all customers :
# ------------------------------------------
print("\n--- Total payments for all customers ---")
for customer in Customer.select():
    payments = Payment.select().where(Payment.customer == customer)
    total = 0

    for p in payments:
        total += p.amount
        print(f"{customer.name},------->, {total}")

# --------------------------------------------
# 5. Find customer with highest total payment:
# --------------------------------------------

max_customer = None
max_amount = 0

for customer in Customer.select():
    total = sum(p.amount for p in customer.payments)
    if total > max_amount:
        max_amount=total
        max_customer=customer

    print(f"{max_customer.name},---------------->,{total}")

db.close()