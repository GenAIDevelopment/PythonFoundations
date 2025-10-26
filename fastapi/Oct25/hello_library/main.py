from fastapi import FastAPI, status, HTTPException
from models import books


app = FastAPI(
    title="Hello Library",
    summary="Getting started with FastAPI",
    version="1.0.0")

@app.get("/")
def home() -> str:
    return "Welcome to Library"


@app.get("/api/books")
def get_all_books():
    return books

@app.get("/api/books/{book_id}")
def get_book_by_id(book_id: str):
    for book in books:
        if book_id == book['id']:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with {book_id} Not Found")


@app.post("/api/books", status_code=status.HTTP_201_CREATED)
def add_new_book(title:str, author: str, genre: str):
    id = f"B00{len(books)+1}"
    book = {
        'id': id,
        'title': title,
        'author': author,
        'genre': genre
    }
    books.append(book)
    return book

@app.put("/api/books/{book_id}")
def update_book(book_id:str, title:str, author: str, genre: str):
    for book in books:
        if book_id == book['id']:
            # update the book
            book['title'] = title
            book['author'] = author
            book['genre'] = genre
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with {book_id} Not Found")

@app.delete("/api/books/{book_id}")
def delete_book(book_id:str):
    # implement delete in dict
    pass




# if __name__ == "__main__":
#     app
    
