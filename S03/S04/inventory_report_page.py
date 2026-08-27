from tkinter import END, Label, Listbox, Toplevel
from inventory_models import Product

def open_inventory_report():
    inventory_report_page = Toplevel()
    inventory_report_page.title("Inventory Report Page")
    inventory_report_page.geometry("600x400")

    listbox = Listbox(inventory_report_page, width=60, height=15)

    listbox.pack(pady=20)

    for product in Product.select():
        listbox.insert(
            END, f"{product.name}   |   Price:  {product.price}  |   stock: {product.stock}"
        )
