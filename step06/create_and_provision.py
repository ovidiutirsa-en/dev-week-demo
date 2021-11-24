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


Base.metadata.create_all(bind=engine)


authors = [
    {"author_id": 1, "author_name": "Constance Adkins"},
    {"author_id": 2, "author_name": "Syed Lowry"},
    {"author_id": 3, "author_name": "Clara Macleod"},
    {"author_id": 4, "author_name": "Alima Crouch"},
    {"author_id": 5, "author_name": "Andreea Steadman"},
    {"author_id": 6, "author_name": "Jon-Paul East"},
]

books = [
    {"book_id": 1, "title": "Angel Of Earth", "author_id": 1, "page_count": 173, "price": 7.92},
    {"book_id": 2, "title": "Butcher Of The Land", "author_id": 2, "page_count": 190, "price": 6.69},
    {"book_id": 3, "title": "Priests Of The World", "author_id": 3, "page_count": 101, "price": 5.43},
    {"book_id": 4, "title": "Robots Of Utopia", "author_id": 4, "page_count": 160, "price": 9.74},
    {"book_id": 5, "title": "Men And Spies", "author_id": 5, "page_count": 131, "price": 8.95},
    {"book_id": 6, "title": "Serpents And Heroes", "author_id": 1, "page_count": 149, "price": 3.98},
    {"book_id": 7, "title": "Love Of Tomorrow", "author_id": 6, "page_count": 185, "price": 4.0},
    {"book_id": 8, "title": "Argument Of The End", "author_id": 3, "page_count": 153, "price": 8.5},
    {"book_id": 9, "title": "Weep For My Past", "author_id": 5, "page_count": 188, "price": 8.93},
    {"book_id": 10, "title": "Vanish In The Mines", "author_id": 1, "page_count": 189, "price": 8.01},
]

db = SessionLocal()

# Add authors
for author in authors:
    db_author = AuthorDBM(**author)
    db.add(db_author)
db.commit()

for _ in db.query(AuthorDBM).all():
    print(_.author_id, _.author_name)
print()

# Add books
for book in books:
    db_book = BookDBM(**book)
    db.add(db_book)

db.commit()

for _ in db.query(BookDBM).all():
    print(_.book_id, _.title)
print()

db.close()
