from tkinter import Tk, Toplevel, Button, Label,Entry
from tkinter import messagebox

from music_online_models import Song

def open_song_count_report():
    
    def song_count_report():
        artist_id = artist_id_entry.get().strip()

        if not artist_id:
            messagebox.showerror(
                "Error",
                "Artist ID is required"
            )
            return

        try:
            count = (
                Song
                .select()
                .where(Song.artist == int(artist_id))
                .count()
            )

            result_label.config(
                text=f"This singer has  {count} songs "
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Artist ID must be numeric"
            )


    search_page = Tk()
    search_page.title("Search Music Report")
    search_page.geometry("500x250")


    # Artist ID
    Label(
        search_page,
        text="Artist ID"
    ).pack(pady=10)

    artist_id_entry = Entry(
        search_page,
        width=30
    )
    artist_id_entry.pack()


    # Report Button
    Button(
        search_page,
        text="Number of songs report",
        command=song_count_report
    ).pack(pady=15)


    # Result Label
    result_label = Label(
        search_page,
        text="",
        font=("Tahoma", 14)
    )
    result_label.pack(pady=20)


    search_page.mainloop()




# from tkinter import Button, Entry, Label, Tk
# from music_online_models import Artist, Song, db

# def show_artist_songs_page():
#     try:
#         artist = Artist.get_by_id(int(artist_id))
#         messagebox.showinfo(
#                     "Success",
#                     "Song saved successfully"
#                 )
#     except Artist.DoesNotExist:
#         l2.config(text="Artist Not Found!!!")

#         messagebox.showerror(
#                     "Success",
#                     "Song saved successfully"
#                 )
#         return
#     songs = Song.select().where(Song.artist==artist).order_by(Song.title)
#     for s in songs:
#         print(s.title)

#     b1.config(text=f"This singer has :{songs.count()} songs ")


# artist_songs_page = Tk()
# artist_songs_page.geometry("400x400")

# a_label =Label(artist_songs_page, text="Artist id : ")
# a_label.pack()

# a_entry =Entry(artist_songs_page)
# a_entry.pack()

# b1 = Button(artist_songs_page,text="Number of Songs",command = lambda :show_artist_songs_page (a_entry.get()))
# b1.pack()

# l2 = Label(artist_songs_page, text = "blah blah")
# l2.pack()


# artist_songs_page.mainloop()