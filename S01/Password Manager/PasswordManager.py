from cryptography.fernet import Fernet


# def write_key():
#     key = Fernet.generate_key()
#     with open('./Mypass.key', "wb") as f:
#         f.write(key)

# write_key()

def Load_key():
    with open('./Mypass.key', 'rb') as f:
        return f.read()



key = Load_key()

fernet = Fernet(key)


def add_pass(username, password):
    with open('./Mytext.txt', "+a") as f:
        encrypted_pass = fernet.encrypt(password.encode()).decode()
        f.write(f"{username} | {encrypted_pass}\n")
    print("Added")



def view_pass():
    with open('./Mytext.txt', "r") as f:
        for item in f:
            item = item.rstrip()
            username, encrypted_password = item.split(" | ")
            password = fernet.decrypt(encrypted_password).decode()
            print(f'username = {username} | password = {password}')


while True:
    user_input = input("Please input your mode : a = add, v= view , q = quit : ")

    if user_input == "v":
        print("These are the following Usernames and Passwords")
        view_pass()
    elif user_input == "a":
        username = input("Please enter a new Username : ")
        password = input("Please enter a new Password : ")
        add_pass(username, password)
    elif user_input == "q":
        break
else:
    print("you have chosen the wrong mode!")