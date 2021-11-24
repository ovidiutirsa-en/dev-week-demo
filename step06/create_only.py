from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHEMY_DB_URL = r"sqlite:///C:\\Users\\otirsa\\devweek.db"
engine = create_engine(
    SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


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


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
