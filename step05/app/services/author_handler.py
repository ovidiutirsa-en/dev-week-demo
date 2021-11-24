"""Author related CRUD operations."""
from sqlalchemy.orm import Session
from ..database.models import AuthorDBM
from ..schema.author import AuthorCreate


def get_author(db: Session, author_id: int):
    return db.query(AuthorDBM).filter(AuthorDBM.author_id == author_id).first()


def get_author_by_name(db: Session, author_name: str):
    return db.query(AuthorDBM).filter(AuthorDBM.author_name == author_name).first()


def get_authors(db: Session, page_id: int = 0, page_size: int = 5):
    skip = page_id * page_size
    limit = page_size
    return db.query(AuthorDBM).offset(skip).limit(limit).all()


def create_author(db: Session, author: AuthorCreate):
    db_author = AuthorDBM(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_authors_count(db: Session):
    return db.query(AuthorDBM).count()
