from tkinter import *
from tkinter import messagebox

from wallet_models import (
    Customer,
    Wallet,
    Transaction
)


def open_statement_page():

    def show_statement():

        national_code = national_code_entry.get().strip()

        customer = Customer.get_or_none(
            Customer.national_code == national_code
        )

        if not customer:
            messagebox.showerror(
                "Error",
                "Customer not found"
            )
            return

        wallet = Wallet.get(
            Wallet.customer == customer
        )

        listbox.delete(0, END)

        for tx in wallet.transactions:

            listbox.insert(
                END,
                f"{tx.tx_type} : {tx.amount} Toman"
            )

    page = Toplevel()
    page.title("Mini Statement")
    page.geometry("500x400")

    Label(
        page,
        text="National Code"
    ).pack(pady=5)

    national_code_entry = Entry(page)
    national_code_entry.pack()

    Button(
        page,
        text="Show Statement",
        command=show_statement
    ).pack(pady=10)

    listbox = Listbox(
        page,
        width=50,
        height=15
    )

    listbox.pack(pady=10)