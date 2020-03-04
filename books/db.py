from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import sys

from .models import Base, Book
from datetime import datetime

load_dotenv()


def _create_session():
    db_url = os.getenv("DATABASE_URL")

    if 'pytest' in sys.argv[0]:
        db_url += '_test'

    if not db_url:
        raise EnvironmentError('Need to set (TEST_)DATABASE_URL')

    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    create_session = sessionmaker(bind=engine)
    return create_session()


session = _create_session()


def get_books(year=None):
    if year is not None:
        books = session.query(Book)
        beg_of_year = datetime(datetime.today().year, "01", "01")
        books = books.filter(Book.read >= beg_of_year).all()
    else:
        books = session.query(Book)

    books = books.order_by(Book.read.desc())
    return books.all()


def add_books(books):
    books = books if isinstance(books, list) else books.items()
    for book in books:
        session.add(Book(goodreads_book_id=book["id"],
                         title=book["title"],
                         author=book["author"],
                         rating=book["rating"],
                         read=book["read"],
                         isbn=book["isbn"]))
    session.commit()
