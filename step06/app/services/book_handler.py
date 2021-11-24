"""Book related CRUD operations."""
from sqlalchemy.orm import Session
from ..database.models import BookDBM
from ..schema.book import BookCreate


def get_book(db: Session, book_id: int):
    return db.query(BookDBM).filter(BookDBM.book_id == book_id).first()


def get_book_by_name_and_author_id(db: Session, title: str, author_id: int):
    return db.query(BookDBM).filter(
        BookDBM.title == title,
        BookDBM.author_id == author_id,
    ).first()


def get_books(db: Session, page_id: int = 0, page_size: int = 5):
    skip = page_id * page_size
    limit = page_size
    return db.query(BookDBM).offset(skip).limit(limit).all()


def get_books_count(db: Session):
    return db.query(BookDBM).count()


def create_book(db: Session, book: BookCreate):
    db_book = BookDBM(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
