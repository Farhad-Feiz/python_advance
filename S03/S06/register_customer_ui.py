from tkinter import Tk,Toplevel,Entry,Label,END,Button,messagebox
from wallet_models import Customer,Wallet

def open_register_customer():
    def register():
        f_name=f_name_entry.get().strip()
        l_name=l_name_entry.get().strip()
        n_code=n_code_entry.get().strip()
        if not f_name or not l_name or not n_code:
            messagebox.showerror(
                "Error",
                "All fields are required"
                )
            return
        customer=Customer.get_or_none(
            Customer.national_code==n_code
            )
        if customer:
            messagebox.showerror(
                "Error",
                "National code already exists!"
            )
            return
        customer=Customer.create(
            first_name=f_name,
            last_name=l_name,
            national_code=n_code
            )
        Wallet.create(
            customer=customer,
            balance=0
        )
        messagebox.showinfo(
            "Welldone!","Cusromer is registered successfully!"
        )
        f_name_entry.delete(0,END)
        l_name_entry.delete(0,END)
        n_code_entry.delete(0,END)
        
    page =Tk()
    page.title("Registration_Form")
    page.geometry("400x200")

    Label(page,text="Registration Form").pack()
    Label(page,text="First name : ").pack()
    f_name_entry=Entry(page)
    f_name_entry.pack()

    Label(page,text="Last name = ").pack()
    l_name_entry=Entry(page)
    l_name_entry.pack()

    Label(page,text="National code = ").pack()
    n_code_entry=Entry(page)
    n_code_entry.pack()

    Button(page, text="Register",command=register).pack(pady=15)


