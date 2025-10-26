from pydantic import BaseModel, Field

class Book(BaseModel):
    id: str = Field(...,max_length=4, min_length=4,description="Id of the book")
    title: str = Field(...,min_length=1, max_length=100, description="Title of the book")
    author: str = Field(...,min_length=1, max_length=100, description="Author of the book")
    genre: str = Field(...,min_length=1, max_length=100, description="Genre of the book")

class BookRequest(BaseModel):
    title: str = Field(...,min_length=1, max_length=100, description="Title of the book")
    author: str = Field(...,min_length=1, max_length=100, description="Author of the book")
    genre: str = Field(...,min_length=1, max_length=100, description="Genre of the book")


books = [
    {
        "id": "B001",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Southern Gothic"
    },
    {
        "id": "B002",
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian Fiction"
    },
    {
        "id": "B003",
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance"
    },
    {
        "id": "B004",
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "genre": "Science Fiction"
    },
    {
        "id": "B005",
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "genre": "Non-Fiction"
    },
    {
        "id": "B006",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Tragedy"
    },
]


# Create a list of Book objects
book_objects = [Book(**data) for data in books ]
