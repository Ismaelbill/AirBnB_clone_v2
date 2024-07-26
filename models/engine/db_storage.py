#!/usr/bin/python3
""" db storage """

import os
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session


classes = {
            "City": City,
            "State": State,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
        }

class DBStorage:
    """ cls """
    __engine = None
    __session = None

    def __init__(self):
        """ init method"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session """
        new_obj = {}
        for clas in classes:
            if cls is None or cls is classes[clas] or cls is clas:
                objs = self.__session.query(classes[clas]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_obj[key] = obj
        return (new_obj)

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session  """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj:
            self.__session.delete(obj)
            self.save()
    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_m = sessionmaker(bind=self.__engine,
                                 expire_on_commit=False)
        Session = scoped_session(session_m)
        self.__session = Session()

    def close(self):
        """ method on the private session attribute """
        self.__session.remove()
