from tkinter import *

from register_customer_ui import open_register_customer
from transaction_ui import open_transaction_page
from statement_ui import open_statement_page

root = Tk()

root.title("Bank System")
root.geometry("400x300")

Button(
    root,
    text="Open Account",
    command=open_register_customer,
    width=20
).pack(pady=10)

Button(
    root,
    text="Deposit / Withdraw",
    command=open_transaction_page,
    width=20
).pack(pady=10)

Button(
    root,
    text="Mini Statement",
    command=open_statement_page,
    width=20
).pack(pady=10)

root.mainloop()