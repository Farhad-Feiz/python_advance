from tkinter import Button, Tk
from song_form import open_save_song
from artist_form import open_save_artist
from search_music_ui import open_song_count_report

main_page = Tk()
main_page.geometry('400x200')
main_page.iconify()

b1 = Button( text='Artist', command= open_save_artist)
b1.place(x=60, y=60)
b2 = Button( text='Song', command= open_save_song)
b2.place(x=220, y=60)
b3 = Button( text='search', command= open_song_count_report)
b3.place(x=340, y=60)

main_page.mainloop()