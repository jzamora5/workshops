""" Employee Model """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Employee(Base):
    """ Employee Model """
    __tablename__ = 'employees'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    manager_id = Column(Integer, ForeignKey('employees.id'))
    employees = relationship("Employee")
