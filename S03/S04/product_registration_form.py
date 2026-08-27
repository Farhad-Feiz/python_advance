from tkinter import Entry, Label, Toplevel,Button,messagebox
from inventory_models import Product,Sale

def open_register_product():
    def register_product():
        name         = name_entry.get()
        price_text   = price_entry.get()
        stock_text   = stock_entry.get()

        if not name or not price_text or not stock_text:
            messagebox.showerror("Error","All fields are required")
            return

        try:

            price = int(price_text)
            stock = int(stock_text)

            Product.create(name = name ,price=price ,stock= stock)
            name_entry.delete(0,"end")
            price_entry.delete(0,"end")
            stock_entry.delete(0,"end")

            messagebox.showinfo("Welldone!",f"{name} is registered")

        except ValueError:
            messagebox.showerror("Error","Price and Stock must be numerick")
        
    Product_registration_form = Toplevel()
    Product_registration_form.geometry("500x200")
    Product_registration_form.title("PRF_FORM")

    Label(Product_registration_form, text="Name").place(x=80 , y=10)
    Label(Product_registration_form, text= "Price").place(x=80 , y=30)
    Label(Product_registration_form,text="Stock").place(x=80 , y=50)

    name_entry = Entry(Product_registration_form, width=30)
    name_entry.place(x=150 , y=10)

    price_entry = Entry(Product_registration_form, width=30)
    price_entry.place(x=150 , y=30)

    stock_entry= Entry(Product_registration_form,width=30)
    stock_entry.place(x=150 , y=50)

    Button(Product_registration_form,text="Registered",command=register_product).place(x=150 , y=120,width=180)


