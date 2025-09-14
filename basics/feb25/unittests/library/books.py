# """This module will have books related methods & classes
# """

# class LibraryItemBase:
#     """Base class for all library items
#     """
#     def __init__(self, id:str, category: str):
#         self.id = id
#         self.category = category
    
#     def __str__(self):
#         return f"id = {self.id}, category = {self.category}"
    

# class Book(LibraryItemBase):
#     """_summary_

#     Args:
#         LibraryItemBase (_type_): _description_
#     """
#     def __init__(self, id, category):
#         super().__init__(id, category)


# def test_book_creation():
#     """This test method will check book creation
#     """
#     book1 = Book("B1", "fiction")
#     assert(str(book1) == f"id = B1, category = fiction")


    