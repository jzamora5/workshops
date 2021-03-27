from one_to_one.models import contact_info
from one_to_one.models.student import Base, Student
from one_to_one.models.contact_info import ContactInfo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


USERS = [
    {"id": 1, "first_name": "Tang", "last_name": "Sophie"},
    {"id": 2, "first_name": "Larry", "last_name": "Hudson"},
    {"id": 3, "first_name": "Peter", "last_name": "Parker"},
    {"id": 4, "first_name": "Mary", "last_name": "Jane"},
    {"id": 5, "first_name": "Tony", "last_name": "Stark"},
    {"id": 6, "first_name": "Steve", "last_name": "Rogers"},
]

CONTACT_INFO = [
    {"id": 1, "student_id": 6, "city": "New York", "phone": "+3549812"},
    {"id": 2, "student_id": 4, "city": "San Francisco", "phone": "+6745821"},
    {"id": 3, "student_id": 2, "city": "Chicago", "phone": "+98732415"},
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

for user in USERS:
    new_user = Student(**user)
    session.add(new_user)

for contact in CONTACT_INFO:
    new_contact_info = ContactInfo(**contact)
    session.add(new_contact_info)

session.commit()


query = session.query(Student, ContactInfo).join(ContactInfo)

for student, contact_info in query:
    print(student.first_name,
          student.last_name,
          contact_info.city,
          contact_info.phone)

print("*" * 10)

students = session.query(Student).all()

for student in students:

    if student.contact_info:
        print(student.first_name,
              student.last_name,
              student.contact_info.city,
              student.contact_info.phone)


print("*" * 10)

contact_info = session.query(ContactInfo).all()
for contact in contact_info:

    print(contact.student.first_name,
          contact.student.last_name,
          contact.city,
          contact.phone)


session.close()

# In ORM Folder

# python3 -m one_to_one.main
