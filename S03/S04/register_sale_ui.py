from tkinter import Label,Button,messagebox,Toplevel,Entry
from inventory_models import Product, Sale

def open_sales_registration():
    def  sales_registration():
        product_id    = product_entry.get().strip()
        quantity_text = quantity_entry.get().strip()

        if not product_id or not quantity_text:
            messagebox.showerror("Error!!!", "All fields are required!")
            return
        try:
            product = Product.get_by_id(int(product_id))
            quantity= int(quantity_text)
            print(quantity, type(quantity))
            print(product.stock, type(product.stock))
            
            if quantity > product.stock:
                result_label.config(text="Not enough stock")
                return
            Sale.create(
                product = product,
                quantity=quantity
            )
            product.stock-=quantity
            product.save()

            result_label.config(text="Sale registered successfully")

            product_entry.delete(0 , "end")
            quantity_entry.delete(0,"end")

        except Product.DoesNotExist:
            messagebox.showerror("Error!", "Product not found")

        except ValueError:
            messagebox.showerror("Error!","Numerick calues are required!")




    sales_reistration_page = Toplevel()
    sales_reistration_page.title("Sales Registration page")
    sales_reistration_page.geometry("400x200")

    Label(sales_reistration_page,text="Product_id",width=35).pack()
    product_entry= Entry(sales_reistration_page,width=35)
    product_entry.pack()

    Label(sales_reistration_page,text="Quantity",width=35).pack()
    quantity_entry  = Entry(sales_reistration_page,width=35)
    quantity_entry.pack()

    b1 = Button(sales_reistration_page, text="Sales Registration",command=sales_registration).place(x=30,y=100)

    result_label = Label(
        sales_reistration_page,
        text=""
    )
    result_label.pack()