import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


conn = create_engine('sqlite:///db.sqlite', echo=True)
Session = sessionmaker()
session = Session(bind=conn)
Base = declarative_base()


association = db.Table(
    'association', Base.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
)


class Book(Base):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    cover_id = db.Column(db.Integer, db.ForeignKey('covers.id'))
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    want_to_read = db.Column(db.Boolean, nullable=False, default=False)

    reviews = relationship('Review', backref='book', lazy=True)
    readers = relationship('User', secondary=association, back_populates='books', lazy=True)
    cover = relationship('Cover', backref=backref('book', uselist=False))

    def __repr__(self):
        return f'{self.title}'


class Review(Base):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    text = db.Column(db.String(3000), nullable=False)

    def __repr__(self):
        return f'By {self.id}'


class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    reviews = relationship('Review', backref='reviewer', lazy=True)
    books = relationship('Book', secondary=association, back_populates='readers', lazy=True)

    def __repr__(self):
        return f'{self.reviewer}'


class Cover(Base):
    __tablename__ = 'covers'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, nullable=False)
    artist = db.Column(db.String)


if __name__ == '__main__':
    Base.metadata.create_all(bind=conn)

    book = Book(title='The Hobbit', author='John R. R. Tolkien', want_to_read=True)
    session.add(book)
    session.commit()

    user = User(name='Ruslan')
    session.add(user)
    session.commit()

    review = Review(text='wonderful', user_id=user.id, book_id=book.id)
    session.add(review)
    session.commit()

    review = user.reviews
    print(f'text: {review[0].text}')
    print(f'book: {review[0].book}')

    user.books.append(book)
    session.commit()

    print("*" * 40)
    print(user.books)

    cover = Cover(image='img.jpg', artist='Bob Ros')
    session.add(cover)
    session.commit()

    book.cover_id = cover.id
    session.commit()

    print("*" * 40)
    print(book.cover)
    print(book.cover.image)





