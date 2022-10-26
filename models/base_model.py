#!/usr/bin/python
"""Module of BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """class of BaseModel"""
    def __init__(self):
        """initialization of class attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """print format of the output"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = __class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
