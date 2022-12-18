from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


conn = create_engine('sqlite:///example_04_back_populates.sqlite', echo=False)
Session = sessionmaker()
session = Session(bind=conn)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    addresses = relationship('Address', back_populates='users')

    def __repr__(self):
        return f'{self.name}'


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    person_id = Column(Integer, ForeignKey('persons.id'))

    users = relationship('Person', back_populates='addresses')

    def __repr__(self):
        return f'{self.email}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=conn)

    # person = Person(name="Oleg")
    # session.add(person)
    # session.commit()
    #
    # address = Address(email="lazebaoleg@gmail.com", person_id=person.id)
    # session.add(address)
    # session.commit()

    person = session.query(Person).filter_by(name='Oleg').first()
    print(f'person: {person}')
    print(f'person_name: {person.name}')
    print(f'person_email: {person.addresses[0].email}')

    address = session.query(Address).first()
    print(f'address: {address}')
    print(f'name by address: {address.users.name}')
