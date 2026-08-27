from tkinter import Button, Tk
from add_author_ui import open_add_author_ui
from add_book_ui import open_add_book_ui

main_page = Tk()
main_page.geometry('400x200')
main_page.iconify()

b1 = Button(text='Author management', command=lambda: open_add_author_ui())
b1.place(x=60, y=60)
b2 = Button(text='Book management', command=lambda: open_add_book_ui())
b2.place(x=220, y=60)

main_page.mainloop()