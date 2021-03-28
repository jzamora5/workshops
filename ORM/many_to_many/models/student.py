""" Student Model """

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


student_class = Table('student_class', Base.metadata,
                      Column('student_id', Integer, ForeignKey('students.id')),
                      Column('place_id', Integer, ForeignKey('classes.id'))
                      )


class Student(Base):
    """ Student Model """
    __tablename__ = 'students'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    classes = relationship(
        "Class",
        secondary=student_class,
        back_populates="students")
