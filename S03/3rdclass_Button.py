import tkinter as tk
from tkinter import ttk
import random

def button_func():
    new = tk.Button()
    new.place(x=random.randint(0 , 500) , y = random.randint(0 , 300))

def button_a_func():
    print("Hello!!!!")

def button_c_func():
    button_a.place(x=random.randint(0 , 500) , y = random.randint(0 , 300))
    button_b.place(x=random.randint(0 , 500) , y = random.randint(0 , 300))
    


# setup a window

window = tk.Tk()
window.title("Buttons")
window.geometry('600x400')

# Buttons
button_a =ttk.Button(master=window, text ="A", command= button_a_func)
button_a.pack()
button_b= ttk.Button(master=window, text="B", command=button_func)
button_b.pack()
button_c = ttk.Button(master = window, text ="C", command= button_c_func)
button_c.pack()
"""
button_b = ttk.StringVar(value="FER")
button_b = ttk.Button(window, text="2nd Button", command=button_func)
button_b.pack()
"""
def e11():
    user = e1.get()
    u2 = int(user)
    button_d.config(text="Even")
    

    if  u2%2==0:
        button_d.config(text="Even Number")
            
    else:
        button_d.config(text="Odd Number")
        print("Odd number")

e1= ttk.Entry()
e1.place(x=100 , y = 200)
button_d = ttk.Button(window, text = "Odd or Even", command= e11)
button_d.pack()


# Run
window.mainloop()