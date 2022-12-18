from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


conn = create_engine('sqlite:///webinar.db', echo=True)
Base = declarative_base()
Session = sessionmaker()
session = Session(bind=conn)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return f'<User(nme={self.name}, fullname={self.fullname}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=conn)

    user = User(name='Ivan', fullname='Ivan Ivanov')
    session.add(user)
    session.commit()

    q = session.query(User).filter_by(name='Ivan')
    print(q)
    print(q.first())

    session.add_all([User(name='Petr', fullname='Petrov'),
                     User(name='Oleg', fullname='Oleg Lazeba')])

    session.commit()

    user.fullname = 'Ivan Sidorov'
    print(user.id)
    print(session.dirty)
    session.commit()

    s = session.execute("""SELECT * FROM users""")
    print(s)
    print(s.first())

    session.delete(user)
    session.commit()

    session.rollback()
    print(session.new)



