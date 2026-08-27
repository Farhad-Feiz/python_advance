

artist = Artist.create(name="Hans Zimmer")

album = Album.create(
    title="Interstellar OST",
    artist=artist
)

Track.create(name="Cornfield Chase", album=album)
Track.create(name="No Time for Caution", album=album)
