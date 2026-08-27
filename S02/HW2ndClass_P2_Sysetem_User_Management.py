from peewee import CharField,IntegerField,BooleanField,Model,SqliteDatabase,ForeignKeyField

"""
class User:
    def __init__(self, name, email, active=True):
        self.name = name
        self.email = email
        self.active = active

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, email):
        self.users.append(User(name, email))
        print(f"user with the name {name} is added")

    def deactivate_by_email(self, email):
        email = email.strip().lower()
        for user in self.users:
            if user.email.strip().lower() == email:
                user.active = False
                print(f"user with this {email} is deactivated by the mananger")
                return
        print("Such a user was not found!!")

    def active_users(self):
        return [u for u in self.users if u.active]

    def inactive_users(self):
        return[u for u in self.users if not u.active]

    def total_users(self):
        return len(self.users)

    def count_active(self):
        return len(self.active_users())

    def count_inactive(self):
        return len(self.inactive_users())

    
manager = UserManager()

"""
"""
manager.add_user("Ali", "ali@python.com")
manager.add_user("Helen", "helen@python.com")
manager.add_user("Rostam", "rostam@python.com")
manager.add_user("Faezeh", "faezeh@python.com")
manager.add_user("Faezeh", "faezeh@python.com")
manager.add_user("Firouzeh", "firouzeh@python.com")
manager.add_user("Yalda", "yalda@python.com")
manager.add_user("Farhad", "farhad@python.com")
manager.add_user("Neda", "neda@python.com")
manager.add_user("Lida", "lida@python.com")


manager.deactivate_by_email("ali@python.com")

print("Active users : ")

for u in manager.active_users():
    print(u.name, "-", u.email)


# print("deactivated user : ")

print("Total number of users : ",manager.total_users())
print("Total active of users : ",manager.count_active())
print("Total inactive of users : ",manager.count_inactive())
"""