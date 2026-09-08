"""
class Person:
    def __init__(self, name):
        self._name = name
p = Person("Farhad")

print(p._name)
class Person:
    def __init__(self, name):
        self._name = name

class Student(Person):
    def show_name(self):
        print(self._name)

s = Student("Farhad")
s.show_name()

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
account = BankAccount(1000)

print(account._BankAccount__balance)
# print(account.__balance)

class Wallet:
    def __init__(self):
        self.owner = "Farhad"      # public
        self._currency = "IRT"     # protected
        self.__balance = 1000      # private

wallet = Wallet()

print(wallet.owner)       # ✅
print(wallet._currency)   # ⚠️
# print(wallet.__balance)   # ❌ خطا
print(wallet._Wallet__balance)  #"with this line 'balance' is called"
"""
"""



class Account:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._account_type = "Normal"  # protected
        self.__balance = balance    # private

    def deposit(self, amount):
        self.__balance += amount

    def _get_balance(self):
        "متد protected"
        return self.__balance

    def show_info(self):
        print(f"Owner: {self.owner}")
        print(f"Type: {self._account_type}")
        print(f"Balance: {self.__balance}")


class SavingsAccount(Account):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)

        # دسترسی به protected
        self._account_type = "Savings"

    def show_account_type(self):
        print(self._account_type)

    def show_balance(self):
        # دسترسی مستقیم به private ممکن نیست
        # print(self.__balance)  # خطا

        # از متد protected استفاده می‌کنیم
        print(self._get_balance())
account = SavingsAccount("Farhad", 1000)

print(account.owner)
account.show_account_type()
account.show_balance()
class Customer:
    def __init__(self, name, national_code):
        self.name = name                    # public
        self._wallet_count = 0              # protected
        self.__national_code = national_code  # private

    def add_wallet(self):
        self._wallet_count += 1

    def get_national_code(self):
        return self.__national_code



class VIPCustomer(Customer):

    def show_status(self):
        print(self.name)           # public
        print(self._wallet_count)  # protected

        # print(self.__national_code)  # خطا
        print(self.get_national_code())

wallet = VIPCustomer("Farhad" ,59230592)
wallet.show_status()
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name            # public
        self._department = "General" # protected
        self.__salary = salary      # private

    def get_salary(self):
        return self.__salary


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self._department = "Management"

    def show_info(self):
        print("Name:", self.name)           # public
        print("Department:", self._department)  # protected

        # print(self.__salary)  # خطا!
        print("Salary:", self.get_salary())


manager = Manager("Farhad", 50000)

manager.show_info()
