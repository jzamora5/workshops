""" Order Model """

from .customer import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Order(Base):
    """ Order Info Model """
    __tablename__ = 'orders'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship("Customer", back_populates="orders")
