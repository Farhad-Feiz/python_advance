from tkinter import Label,Button,messagebox,Toplevel,Entry,END
from todo_models import User

def open_register_page():
    def register():
        user_text=username_entry.get().strip()
        pass_text=password__entry.get().strip()
        if not user_text or not pass_text:
            messagebox.showerror(
                "Error," 
                "All fields are required"
            )
            return
        user = User.get_or_none(User.username==user_text)
        if user:
            messagebox.showerror(
                "Error",
                "Username already exists"
            )
            return
        User.create(
            username = user_text,
            password = pass_text
        )
        messagebox.showinfo("Success","User registered successfully")
        username_entry.delete(0,END)
        password__entry.delete(0,END)
    registry_form=Toplevel()
    registry_form.geometry("400x200")
    registry_form.title("Registry Form")   
    username_l = Label(registry_form,text="Username :").pack()
    username_entry=Entry(registry_form)
    username_entry.pack()
    password_l= Label(registry_form, text="Password :").pack()
    password__entry=Entry(registry_form)
    password__entry.pack()
    result_label = Label(registry_form,text="")
    Button(registry_form,text="Register",command=register).pack(pady=10)
