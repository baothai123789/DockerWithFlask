from ..extensions import db
import sqlalchemy as sa
from sqlalchemy.orm import Mapped,mapped_column,relationship
from typing import List
from dataclasses import dataclass
books_authors = sa.Table('books_authors',db.metadata,
                         sa.Column('book_id',sa.ForeignKey("books.id")),
                         sa.Column('author_id',sa.ForeignKey("authors.id")))
books_categories = sa.Table('books_categories',db.metadata,
                            sa.Column('book_id',sa.ForeignKey('books.id')),
                            sa.Column('category_id',sa.ForeignKey('categories.id')))

@dataclass
class Author(db.Model):
    id: int
    firstname: str
    lastname: str
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(sa.String(256))
    lastname: Mapped[str] = mapped_column(sa.String(256))
    nation_id:Mapped[int] = mapped_column(sa.ForeignKey('nations.id'))
    books: Mapped[List["Book"]] =relationship(secondary=books_authors,backref='author')


class Category(db.Model):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(256),nullable=False)
    books: Mapped[List["Book"]] = relationship(secondary=books_categories,backref='category',lazy=False)

class Book(db.Model):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    bookid: Mapped[str] = mapped_column(sa.String(20),nullable=False,unique=True,index=True)
    title: Mapped[str] = mapped_column(sa.String(256),nullable=False)
    description:Mapped[str] = mapped_column(sa.String(256),nullable=True)
    publish_year: Mapped[int] = mapped_column(nullable=True)
    language_id: Mapped[int] = mapped_column(sa.ForeignKey('languages.id'),nullable=True)
    publisher_id: Mapped[int] = mapped_column(sa.ForeignKey('publishers.id'),nullable=True)
    authors: Mapped[List["Author"]] = relationship(secondary=books_authors,backref='book',lazy=True)
    categories: Mapped[List["Category"]] = relationship(secondary=books_categories,backref='book',lazy=True)

class Nation(db.Model):
    __tablename__ = 'nations'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(256))
    authors: Mapped["Author"] = relationship(backref='nation',lazy=False)



class Language(db.Model):
    __tablename__ = 'languages'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(sa.String(256))
    books: Mapped[List["Book"]] = relationship(backref='language',lazy=False)

class Publisher(db.Model):
    __tablename__ = 'publishers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(256),nullable=False)
    books: Mapped[List["Book"]] = relationship(backref='publisher',lazy=False)




