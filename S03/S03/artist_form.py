from tkinter import Tk, Toplevel, Button, Label,Entry
from tkinter import messagebox

from music_online_models import Artist

def open_save_artist():

    def save_artist():
        name = artist_name_entry.get().strip()

        if not name:
            messagebox.showerror(
                "Error",
                "Artist name is required"
            )
            return

        Artist.create(name=name)

        artist_name_entry.delete(0, "end")

        messagebox.showinfo(
            "Success",
            "Artist saved successfully"
        )


    artist_page = Toplevel()
    artist_page.title("Artist Registration")
    artist_page.geometry("350x150")

    Label(
        artist_page,
        text="Artist Name"
    ).pack(pady=10)

    artist_name_entry = Entry(
        artist_page,
        width=35
    )
    artist_name_entry.pack()

    Button(
        artist_page,
        text="Save Artist",
        command=save_artist
    ).pack(pady=15)

    artist_page.mainloop()