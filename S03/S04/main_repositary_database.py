from tkinter import Button,Tk,ttk
from product_registration_form import open_register_product
from register_sale_ui import open_sales_registration
from inventory_report_page import open_inventory_report


main_page=Tk()
main_page.title("Rep_Database_Main")
main_page.geometry("500x100")

b1=ttk.Button(text="Product Registration",command=open_register_product)
b1.place(x=10 , y=30,bordermode="outside")

b2=ttk.Button(text="Sales Registration",command=open_sales_registration)
b2.place(x=160 , y=30,bordermode="outside")

b3=ttk.Button(text="Inventory Report",command=open_inventory_report)
b3.place(x=310 , y=30,bordermode="outside")

main_page.mainloop()
