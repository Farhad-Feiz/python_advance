from tkinter import Button, Tk
from add_food_ui import open_add_food_ui
from update_price_ui import open_update_price_ui

main_page = Tk()
main_page.geometry('400x200')
main_page.iconify()

b1 = Button(text='Add Food', command=lambda: open_add_food_ui())
b1.place(x=60, y=60)
b2 = Button(text='Update price', command=lambda: open_update_price_ui())
b2.place(x=220, y=60)


main_page.mainloop()
