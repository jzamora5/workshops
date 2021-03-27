""" Student Model """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Student(Base):
    """ Student Model """
    __tablename__ = 'students'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    contact_info = relationship(
        "ContactInfo", uselist=False, back_populates="student")
