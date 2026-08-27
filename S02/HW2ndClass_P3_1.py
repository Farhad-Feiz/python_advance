from peewee import BooleanField, CharField, ForeignKeyField, IntegerField, Model, SqliteDatabase




# --------------------------------------------------------

# Database

# --------------------------------------------------------

databse = SqliteDatabase("order.db")





# --------------------------------------------------------

# User Model

# --------------------------------------------------------

class User(Model):



    id = IntegerField(unique=True)

    name = CharField

    email = CharField(unique=True)

    active = BooleanField(default=True)



# --------------------------------------------------------

# Order Model

# --------------------------------------------------------

class Order(Model):



    product_name = CharField

    quantity = IntegerField

    user = ForeignKeyField(User, backref="orders")



# --------------------------------------------------------

# CreatTables

# --------------------------------------------------------

db.connect()



db.creat_tables([User, Order])



# --------------------------------------------------------

# UserManagementClass

# --------------------------------------------------------

class UserManager:

    @staticmethod
    def add_user(name, email):
        email_clean = email.strip().lower()
        if User.select().where(User.email == email_clean).exists():
            print("This email is already registered!")
            return
        user = User.create(name=name, email=email_clean)
        print(f"user {name} with email:{email_clean} was added")
        return user

    @staticmethod
    def deactivate_by_email(email):
        email_clean = email.strip().lower()
        try:
            user = User.get(User.email == email_clean)
        except User.DoesNotExist:
            print("User with this email was not founded")
            return
        user.active = False
        user.save()

    @staticmethod
    def active_users():
        return list(User.select().where(User.active is True))

    @staticmethod
    def inactive_users():
        return list(User.select().where(User.active is False))

    @staticmethod
    def total_users():
        return User.select().count()

    @staticmethod
    def count_active():
        return User.select().where(User.active is True).count()


    @staticmethod
    def count_inactive():
        return User.select().where(User.active is False).count()


    

db.close()

# --------------------------------------------------------

# User Model

# --------------------------------------------------------

# --------------------------------------------------------

# User Model

# --------------------------------------------------------