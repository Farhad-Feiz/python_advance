from tkinter import *
from tkinter import messagebox

from todo_models import User
from dashboard_ui import open_dashboard

def open_login_page():

    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        user =User.get_or_none(
            (User.username==username) &
            (User.password==password)
        )

        if user is None:
            messagebox.showerror(
                "Erroe!",
                "Username or Password is incorrect"
            )
            return
        login_page.destroy()
        open_dashboard(user.id)

    login_page=Toplevel()
    login_page.title("Login Page")
    login_page.geometry("400x200")

    Label(login_page,text= "Username : ").pack()
    username_entry= Entry(login_page)
    username_entry.pack()

    Label(login_page,text="Password : ").pack()
    password_entry=Entry(
        login_page,
        show="*"
        )
    password_entry.pack()
    Button(
        login_page,
        text="Login",
        command=login
    ).pack(pady=10)