from cryptography.fernet import Fernet

# def write_key():
#     key =Fernet.generate_key()
#     with open('./key.key' ,"wb" ) as f:
#         f.write(key)
# write_key()


def load_key():
    with open("./key.key", "rb") as f:
        return f.read()
    
key = load_key()

fernet = Fernet(key)


def add_pass(username, password):
    with open("./password.txt","+a") as f:
        encrypted_pass = fernet.encrypt(password.encode()).decode()
        f.write(f'{username}|{encrypted_pass}\n')
    print("Added")

def view_pass():
    with open("./password.txt","r") as f:
        for item in f:
            item = item.rstrip()
            username,encrypted_password = item.split("|")
            password = fernet.decrypt(encrypted_password).decode()
            print(f'username : {username} | password : {password}')
            
while True:
    user_input = input("Enter the mode (v: view, a: add, q: quit)")
    if user_input == "v":
        print("Your passwords are as following: ")
        view_pass()

    elif user_input == "a":
        username = input("Please enter your username : ")
        password = input("Please input your paasword : ")
        add_pass(username,password)
        
    elif user_input == "q":
        break
    else:
        print("Wrong mode!")