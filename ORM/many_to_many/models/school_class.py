""" Class Model """

from .student import Base, student_class
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Class(Base):
    """ Class Info Model """
    __tablename__ = 'classes'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    title = Column(String(128), nullable=False)
    class_desc = Column(String(128), nullable=False)
    students = relationship(
        "Student",
        secondary=student_class,
        back_populates="classes")
