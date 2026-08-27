from tkinter import Button, Entry, Label, Tk
from models import Author, db,Book

def open_add_book_ui():

    def add_to_db():
        t = e_title.get()
        p = e_pages.get()
        a_i=int(e_author_id.get())

        l3=Label(book_page,text="Book is registered succesfully")
        l3.pack()

        if t == "" or p =="" or a_i=="":
            l3 = Label(book_page, text="Please fill all fields!",  fg="red")
            l3.place(x=190 , y=250)
            return
                
        try:
            author = Author.get(Author.id == a_i)
        except:
            l3 = Label(book_page, text="Author ID not found!", fg="red")
            l3.place(x=190, y=250)
            return
        
        with db.connection_context():
            Book.create(title=t, pages=p, author= a_i)

    book_page = Tk()
    book_page.geometry("600x400")



    l_title = Label(book_page, text='Title :')
    l_title.place(x=190, y=100)

    e_title = Entry(book_page)
    e_title.place(x=280, y=100)

    l_pages = Label(book_page, text='Pages :')
    l_pages.place(x=190, y=125)

    e_pages = Entry(book_page)
    e_pages.place(x=280, y=125)

    l_author_id = Label(book_page, text='Author id :')
    l_author_id.place(x=190, y=150)

    e_author_id = Entry(book_page)
    e_author_id.place(x=280, y=150)

    registry = Button(book_page, text='Register', command=add_to_db)
    registry.pack()



    book_page.mainloop()