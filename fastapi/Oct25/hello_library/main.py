from fastapi import FastAPI, status, HTTPException
from models import books, Book, book_objects, BookRequest


app = FastAPI(
    title="Hello Library",
    summary="Getting started with FastAPI",
    version="1.0.0")

@app.get("/")
def home() -> str:
    return "Welcome to Library"


@app.get("/api/books")
def get_all_books() -> list[Book]:
    return book_objects

@app.get("/api/books/{book_id}")
def get_book_by_id(book_id: str):
    for book in books:
        if book_id == book['id']:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with {book_id} Not Found")


@app.post("/api/books", status_code=status.HTTP_201_CREATED)
def add_new_book(book:BookRequest) -> Book:
    id = f"B00{len(book_objects)+1}"
    new_book = Book(
        id=id,
        author=book.author,
        title=book.title,
        genre=book.genre)
    book_objects.append(new_book)
    return new_book

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
    books = [b for b in books if b["id"] != book_id]

    if len(books) == initial_length:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cannot delete: Book with ID '{book_id}' not found."
        )




# if __name__ == "__main__":
#     app
    
