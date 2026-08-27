from tkinter import Tk, Toplevel, Button, Label,Entry
from tkinter import messagebox

from music_online_models import Artist, Song

def open_save_song():
    def save_song():
        title = title_entry.get().strip()
        duration = duration_entry.get().strip()
        artist_id = artist_id_entry.get().strip()

        if not title or not duration or not artist_id:
            messagebox.showerror(
                "Error",
                "All fields are required"
            )
            return

        try:
            artist = Artist.get_by_id(
                int(artist_id)
            )

            Song.create(
                title=title,
                duration=int(duration),
                artist=artist
            )

            title_entry.delete(0, "end")
            duration_entry.delete(0, "end")
            artist_id_entry.delete(0, "end")

            messagebox.showinfo(
                "Success",
                "Song saved successfully"
            )

        except Artist.DoesNotExist:
            messagebox.showerror(
                "Error",
                "Artist ID not found"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Duration and Artist ID must be numeric"
            )


    root = Toplevel()
    root.title("Song Registration")
    root.geometry("350x250")

    Label(root, text="Song Title").pack(pady=5)

    title_entry = Entry(
        root,
        width=35
    )
    title_entry.pack()

    Label(root, text="Duration (seconds)").pack(pady=5)

    duration_entry = Entry(
        root,
        width=35
    )
    duration_entry.pack()

    Label(root, text="Artist ID").pack(pady=5)

    artist_id_entry = Entry(
        root,
        width=35
    )
    artist_id_entry.pack()

    Button(
        root,
        text="Save Song",
        command=save_song
    ).pack(pady=15)


