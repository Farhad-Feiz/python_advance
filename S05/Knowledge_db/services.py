import requests
from knowledge_db import (
    Book,
    Note,
    Tag,
    NoteTag
)
def fetch_book_by_isbn(isbn):
    url = (
        "https://openlibrary.org/api/books"
        f"?bibkeys=ISBN:{isbn}"
        "&format=json"
        "&jscmd=data"
    )
    response=requests.get(
        url,
        timeout=10
    )
    response.raise_for_status()
    data = response.json()
    print(data)
    key=f"ISBN:{isbn}"
    if key not in data:
        raise ValueError(
            "Book Not Found"
        )
    book_data=data[key]
    title=book_data["title"]
    authors = ", ".join(
        author["name"]
        for author in 
        book_data.get(
            "authors",
            []
        )
    )
    publish_date =(
        book_data.get(
            "publish_date",
            ""publish_date
        )
    )