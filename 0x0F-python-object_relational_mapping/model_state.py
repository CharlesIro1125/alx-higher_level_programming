#!/usr/bin/python3
"""
Defines a state model.
Inherits from SQLAlchemy Base and maps to class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Represents a state for MySQL db.

    __tablename__ :The name of the table in MySQL
    id(sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
