from tkinter import *
from todo_models import User

def open_dashboard(user_id):
    
    dashboard_page = Toplevel()
    dashboard_page.title("Dashboard")
    dashboard_page.geometry("500x400")

    user = User.get_by_id(user_id)

    Label(
        dashboard_page,
        text=f"Welcome {user.username}"
    ).pack(pady=10)

    listbox= Listbox(
        dashboard_page,
        width=50,
        height=15
    )

    listbox.pack()

    for task in user.tasks:
        status = "Done" if task.is_done else "Pending"
        listbox.insert(
            END,
            f"{task.title} ----{status}"
        )