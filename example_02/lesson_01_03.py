import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


conn = create_engine('sqlite:///db.sqlite', echo=True)
Session = sessionmaker()
session = Session(bind=conn)
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(50), nullable=False)
    author = db.Column('author', db.String(100), nullable=False)
    want_to_read = db.Column('want_to_read', db.Boolean, nullable=False)

    def __repr__(self):
        return f'{self.title}'


Base.metadata.create_all(bind=conn)
book = Book(title='The Hobbit', author='John R. R. Tolkien', want_to_read=False)
session.add(book)
session.commit()

rows = session.query(Book).filter(Book.author == 'John R. R. Tolkien').all()
print('Query by SqlAlchemy ORM:', rows)
