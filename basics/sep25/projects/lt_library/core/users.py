"""This module will have all the necessary classes for maintaining
users of the library system
"""

from abc import ABC, abstractmethod

class Person(ABC):
    """Abstract base class representing a person in the library system.

    This class defines the interface for borrowing and returning items.
    Concrete subclasses (e.g., `Member`, `Librarian`) must implement
    these abstract methods.
    """

    @abstractmethod
    def borrow_item(self, item_id: str) -> None:
        """Borrow an item from the library.

        Args:
            item_id (str): The unique identifier of the item to borrow.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """

    @abstractmethod
    def return_item(self, item_id: str) -> None:
        """Return a borrowed item to the library.

        Args:
            item_id (str): The unique identifier of the item being returned.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        
    