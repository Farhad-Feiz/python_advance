import tkinter as tk
from restaurant_models import Food

def open_update_price_ui():
    def update_price():
        food_id = int(id_entry.get())
        new_price = int(price_entry.get())

        q = Food.update(price=new_price).where(Food.id == food_id)
        q.execute()

        msg_label.config(text="Price updated successfully!")

    update_price_page = tk.Tk()
    update_price_page.title("Update Food Price")
    update_price_page.geometry("300x300")

    tk.Label(update_price_page, text="Food ID").pack()
    id_entry = tk.Entry(update_price_page)
    id_entry.pack()

    tk.Label(update_price_page, text="New Price").pack()
    price_entry = tk.Entry(update_price_page)
    price_entry.pack()

    tk.Button(update_price_page, text="Update Price", command=update_price).pack()

    msg_label = tk.Label(update_price_page, text="")
    msg_label.pack()

    update_price_page.mainloop()

