from tkinter import *
from tkinter import messagebox
from wallet_models import(
    Customer,
    Wallet,
    Transaction
)
def open_transaction_page():
    def deposit():
        n_code=n_code_entry.get().strip()
        amount_text=amount_entry.get().strip()
        customer=Customer.get_or_none(
            Customer.national_code==n_code
        )
        if not customer:
            messagebox.showerror(
                "Error",
                "Customer not found"
            )
            return
        try:
            amount = int(amount_text)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Invalid amount"
            )
            return
        if amount<=0:
            messagebox.showerror(
                "Error",
                "Amount must be greater than zero"
            )
            return
        wallet = Wallet.get(
            Wallet.customer == customer
        )
        wallet.balance+=amount
        wallet.save()

        Transaction.create(
            wallet=wallet,
            amount=amount,
            tx_type="Deposit"
        )
        messagebox.showinfo(
            "Success",
            "Deposit is completed"
        )
    def withdraw():
        n_code=n_code_entry.get().strip()
        amount_text=amount_entry.get().strip()
        
        customer=Customer.get_or_none(
            Customer.national_code==n_code
        )
        if not customer:
            messagebox.showerror(
                "Error",
                "Customer not found"
            )
            return
        try:
            amount = int(amount_text)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Invalid amount"
            )
            return
        if amount<=0:
            messagebox.showerror(
                "Error",
                "Amount must be greater than zero"
            )
            return
        wallet = Wallet.get(
            Wallet.customer == customer
        )
        if wallet.balance<amount:
            messagebox.showerror(
                "Error",
                "Insufficient balance"
            )
            return
        wallet.balance -= amount
        wallet.save()
        Transaction.create(
            wallet=wallet,
            amount=amount,
            tx_type="withdraw"
        )
        messagebox.showinfo(
            "Success",
            "Withdraw completed"
        )
    page=Toplevel()
    page.title("Transactions")
    page.geometry("400x250")
    Label(
        page,
        text="National Code : "
    ).pack()
    n_code_entry=Entry(page)
    n_code_entry.pack()
    Label(
        page,
        text="Amount"
    ).pack()
    amount_entry=Entry(page)
    amount_entry.pack()
    Button(
        page,
        text="Deposit",
        command=deposit
    ).pack(pady=5)
    Button(
        page,
        text="Withdraw",
        command= withdraw
    ).pack(pady=5)