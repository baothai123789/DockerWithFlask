from .models import Book
from .repositories import BookRepository
from typing import List
class BookManger:
    def __init__(self,bookrepository:BookRepository) -> None:
        self.bookrepository = bookrepository


    def getAllBooks(self)->List[Book]:
        return self.bookrepository.get_all_book()