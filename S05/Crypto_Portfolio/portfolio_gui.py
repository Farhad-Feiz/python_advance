from tkinter import *
from tkinter import messagebox

from services import(
    buy_asset,
    sell_asset,
    current_value
)
def run_app():
    root=Tk()
    root.title(
        "Crypto Portfolio"
    )
    root.geometry("400x300")
    # ---------------------------
    # Symbol
    # ---------------------------
    Label(
        root,
        text="Symbol"
    ).pack()
    symbol_entry=Entry(root)
    symbol_entry.pack()
    # ---------------------------
    # Amount
    # ---------------------------
    Label(
        root,
        text="Amount"
    ).pack()
    amount_entry=Entry(root)
    amount_entry.pack()
    # ---------------------------
    # Price
    # ---------------------------
    Label(
        root,
        text="Price"
    ).pack()
    price_entry=Entry(root)
    price_entry.pack()
    # ---------------------------
    # Buy
    # ---------------------------
    def buy_click():
        try:
            symbol=(symbol_entry
                    .get()
                    .upper()
            )
            amount = float(
                amount_entry.get()
            )
            price=float(price_entry
                    .get()
            )
            buy_asset(
                symbol,
                amount,
                price
            )
            messagebox.showinfo(
                "Success",
                "Asset Purchased Successfully"
            )
        except ValueError:
            messagebox.showerror(
                "Error",
                "Invalid Input"
            )
    # ---------------------------
    # Sell
    # ---------------------------
    def sell_click():
        try:
            symbol = (
                symbol_entry
                .get()
                .strip()
                .upper()
            )
            amount = float(
                amount_entry.get()
            )
            price = float(
                price_entry.get()
            )
            result = sell_asset(
                symbol,
                amount,
                price
            )
            if result:
                messagebox.showinfo(
                    "Success",
                    "Asset Sold Successfully"
                )
            else:
                messagebox.showerror(
                    "Error",
                    "Not Enough Asset"
                )
        except ValueError:
            messagebox.showerror(
                "Error",
                "Invlaid Input"
            )
    # ---------------------------
    # Current Value
    # ---------------------------
    def value_click():
        symbol = (
            symbol_entry
            .get()
            .strip()
            .upper()
        )
        value = current_value(
            symbol
        )
        if value is None:
            messagebox.showerror(
                "Error",
                "Price Not Available"
            )
        else:
            messagebox.showinfo(
                "Current Value",
                f"{value:2f}"
            )