"""This module will have necessary library assets
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class LibraryItem:
    """Represents an item in the library catalog.

    Attributes:
        id (str): Unique identifier for the library item.
        title (str): Title of the item.
        author (str): Author or creator of the item.
        isbn (Optional[str]): International Standard Book Number, if available.
        publisher (Optional[str]): Name of the publisher, if available.
        category (Optional[str]): Category or genre of the item, if specified.
        type: Type of library item can be among Books, Dvds...
    """
    id: str
    title: str
    author: str
    isbn: Optional[str] = None
    publisher: Optional[str] = None
    category: Optional[str] = None
    type: str = 'Book'




