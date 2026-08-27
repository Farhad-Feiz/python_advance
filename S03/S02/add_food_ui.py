
from tkinter import Button, Entry, Label, Tk
from restaurant_models import Food, Category, db

def open_add_food_ui():

    def save_food():
        name = e_foodname.get()
        price = int(e_price.get())
        cat_id = int(e_category.get())

        Food.create(name=name, price=price, category=cat_id)
        msg_label.config(text="Food is registered")

    add_food_page = Tk()
    add_food_page.title("Food registry")
    add_food_page.geometry("400x250")

    l_foodname = Label(add_food_page, text="Food name")
    l_foodname.pack()

    e_foodname = Entry(add_food_page)
    e_foodname.pack()

    l_price = Label(add_food_page, text="Price")
    l_price.pack()

    e_price = Entry(add_food_page)
    e_price.pack()

    l_category = Label(add_food_page, text="Category ID")
    l_category.pack()

    e_category = Entry(add_food_page)
    e_category.pack()

    register = Button(add_food_page, text="Register", command=save_food)
    register.pack()

    # Create ONE message label outside the function
    msg_label = Label(add_food_page, text="")
    msg_label.pack()

    add_food_page.mainloop()
