""" Contact Info Model """

from .student import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class ContactInfo(Base):
    """ Contact Info Model """
    __tablename__ = 'contact_info'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    city = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'), unique=True)
    student = relationship("Student", back_populates="contact_info")
