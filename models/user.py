#!/usr/bin/python3
"""Module of User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
