from one_to_one.models import contact_info
from one_to_many.models.customer import Base, Customer
from one_to_many.models.order import Order
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


CUSTOMERS = [
    {"id": 1, "name": "Tang"},
    {"id": 2, "name": "Larry"},
    {"id": 3, "name": "Peter"},
    {"id": 4, "name": "Mary"},
    {"id": 5, "name": "Tony"},
    {"id": 6, "name": "Steve"},
]

ORDERS = [
    {"id": 1, "customer_id": 1},
    {"id": 2, "customer_id": 1},
    {"id": 3, "customer_id": 1},
    {"id": 4, "customer_id": 6},
    {"id": 5, "customer_id": 6},
    {"id": 6, "customer_id": 6},
]


DB_USER = "test_user"
DB_PASSWORD = "test_pwd"
DB = "relationships"

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                       format(DB_USER, DB_PASSWORD, DB),
                       pool_pre_ping=True)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for customer in CUSTOMERS:
    new_customer = Customer(**customer)
    session.add(new_customer)

for order in ORDERS:
    new_order = Order(**order)
    session.add(new_order)

session.commit()


query = session.query(Customer, Order).join(Order)

for customer, order in query:
    print(customer.name,
          order.id)

print("*" * 10)

customers = session.query(Customer).all()

for customer in customers:
    if customer.orders:
        for order in customer.orders:
            print(customer.name, order.id)

print("*" * 10)

orders = session.query(Order).all()
for order in orders:

    print(order.customer.name, order.id)


session.close()

# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html

# In ORM Folder

# python3 -m one_to_many.main
