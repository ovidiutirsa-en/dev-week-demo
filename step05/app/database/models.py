from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .config import Base


class AuthorDBM(Base):
    __tablename__ = "authors"

    author_id = Column(Integer, primary_key=True, index=True)
    author_name = Column(String)

    books = relationship("BookDBM", back_populates="author")


class BookDBM(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("authors.author_id"))
    title = Column(String)
    page_count = Column(Integer)
    price = Column(Float)
    author = relationship("AuthorDBM", back_populates="books")
