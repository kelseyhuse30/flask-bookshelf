from sqlalchemy import Column, Sequence, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    goodreads_book_id = Column(String(22))
    title = Column(String(300))
    author = Column(String(300))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    rating = Column(Integer)
    read = Column(DateTime)
    isbn = Column(String(20))

    def __repr__(self):
        return "<Book('%d', '%s')>" % (self.id, self.title)
