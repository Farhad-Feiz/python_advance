from tkinter import *
from register_ui import open_register_page
from login_page_ui import open_login_page

root = Tk()
root.geometry("400x250")
root.title("Task Manager")

Button(
    root,
    text="Register",
    width=20,
    command=open_register_page,
).pack(pady=20)

Button(
    root,
    text="Login",
    width=20,
    command=open_login_page
).pack(pady=20)

root.mainloop()