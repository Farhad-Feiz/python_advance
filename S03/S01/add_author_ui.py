from tkinter import *
from models import db , Author , Book
def open_add_author_ui():
    def add_to_db():
        a = e_author.get()
        n = e_nationality.get()
        l3=Label(author_page,text="Author is registered succesfully")
        l3.pack()
        
        with db.connection_context():
            Author.create(name = a , country = n)
    author_page =Tk()
    author_page.geometry("600x400")

    l_author = Label(author_page, text='Author :')
    l_author.place(x=190 , y= 100)
    # l_author.pack()

    e_author =Entry(author_page)
    e_author.place(x=280 ,  y =100)

    l_nationality = Label(author_page,text='Nationality :')
    l_nationality.place(x=190, y=125)
    # l_nationality.pack()

    e_nationality =Entry(author_page)
    e_nationality.place(x=280 ,  y = 125)

    registry = Button(author_page , text='Register' , command=add_to_db)
    registry.pack()

    author_page.mainloop()
