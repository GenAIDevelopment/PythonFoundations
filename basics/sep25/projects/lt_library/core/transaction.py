"""This will deal with transactional items


"""

from core.assets import LibraryItem
from core.users import Person
from datetime import datetime

class Transaction:
    """Transaction class
    """

    def __init__(self, person: Person, item: LibraryItem):
        self.__person = person
        self.__item = item
        self._id:str = None
        self._when:datetime = datetime.now()

    @property
    def person(self) -> Person:
        """Get Person info

        Returns:
            Person: person
        """
        return self.__person
    
    def item(self) -> LibraryItem:
        """Get Item

        Returns:
            LibraryItem: Library item
        """
        return self.__item
