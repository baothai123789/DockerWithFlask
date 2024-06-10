from .models import Book
from ..extensions import db
from typing import Any, List

class SingletonRepository(type):
    _instance = {}
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonRepository, cls).__call__(*args, **kwargs)
        return cls._instance[cls]

class BookRepository(metaclass=SingletonRepository):
    def get_all_book(self)->List[Book]:
        books = db.session.query(Book).all()
        return books