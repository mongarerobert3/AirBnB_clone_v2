#!/usr/bin/python3
"""DBStorage storage engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from os import getenv
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class DBStorage():
    """New engine DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """initializing the sqlalchemy engine"""
        usr = getenv("HBNB_MYSQL_USER")
        pswrd = getenv("HBNB_MYSQL_PWD")
        hst = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")  # Database

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                usr, pswrd, hst, db), pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def all(self, cls=None):
        """all method from the current database session"""
        new_dict = {}
        obj_dict = {"User": User,
                    "Amenity": Amenity,
                    "Review": Review,
                    "State": State,
                    "Place": Place,
                    "City": City
                    }

        if cls is None:
            for class_name in obj_dict:
                data = self.__session.query(obj_dict[class_name]).all()
                for obj in data:
                    new_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
        elif (cls in obj_dict):
            data = self.__session.query(obj_dict[cls]).all()
            for obj in data:
                new_dict[f"{obj.id}"] = obj
        print(type(new_dict))
        print("Entra")
        return new_dict

    def reload(self):
        """Reload the database session"""
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
