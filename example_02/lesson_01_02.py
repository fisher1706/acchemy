import sqlalchemy as db
from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData

conn = create_engine('sqlite:///db.sqlite', echo=True)
metadata = MetaData()

books = db.Table(
    'books', metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('title', db.String(50), nullable=False),
    db.Column('author', db.String(100), nullable=False),
    db.Column('want_to_read', db.Boolean, nullable=False),
)

metadata.create_all(bind=conn)

conn.execute(
    books.insert(),
    {
        'title': 'The Hobbit',
        'author': 'John R. R. Tolkien',
        'want_to_read': False
    }
)

rows = conn.execute(
    select([books.c.title]).where(books.c.author == 'John R. R. Tolkien')
)

print('Query by SqlAlchemy core methods:')
for row in rows:
    print(row)