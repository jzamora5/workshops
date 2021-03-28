from self_join.models.employee import Base, Employee
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased


EMPLOYEES = [
    {"id": 6, "first_name": "Steve", "last_name": "Rogers", "manager_id": None},
    {"id": 1, "first_name": "Tang", "last_name": "Sophie", "manager_id": 6},
    {"id": 2, "first_name": "Larry", "last_name": "Hudson", "manager_id": 6},
    {"id": 3, "first_name": "Peter", "last_name": "Parker", "manager_id": 6},
    {"id": 4, "first_name": "Mary", "last_name": "Jane", "manager_id": 1},
    {"id": 5, "first_name": "Tony", "last_name": "Stark", "manager_id": 3},
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

for employee in EMPLOYEES:
    new_employee = Employee(**employee)
    session.add(new_employee)


session.commit()

E = aliased(Employee)
M = aliased(Employee)

query = session.query(E).join(M, E.manager_id == M.id)

for employee in query:
    print(employee.first_name,
          employee.last_name,
          employee.manager_id)

print("*" * 10)

employees = session.query(Employee).all()

for employee in employees:

    if employee.employees:
        for subordinate in employee.employees:
            print("Subordinate",
                  subordinate.first_name,
                  subordinate.last_name,
                  "Manager",
                  employee.first_name,
                  employee.last_name)


session.close()

# https://docs.sqlalchemy.org/en/14/orm/self_referential.html

# In ORM Folder

# python3 -m self_join.main
