from many_to_many.models.student import Base, Student
from many_to_many.models.school_class import Class
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


STUDENTS = [
    {"id": 1, "first_name": "Tang", "last_name": "Sophie"},
    {"id": 2, "first_name": "Larry", "last_name": "Hudson"},
    {"id": 3, "first_name": "Peter", "last_name": "Parker"},
    {"id": 4, "first_name": "Mary", "last_name": "Jane"},
    {"id": 5, "first_name": "Tony", "last_name": "Stark"},
    {"id": 6, "first_name": "Steve", "last_name": "Rogers"},
]

CLASSES = [
    {"id": 1, "title": 'Math', "class_desc": 'Learn the beauty of numbers'},
    {"id": 2, "title": 'Physics', "class_desc": 'Discover how the world works'},
    {"id": 3, "title": 'Chemistry', "class_desc": 'Learn to master the elements'},
    {"id": 4, "title": 'Philosophy', "class_desc": 'What is the meaning of life?'},
    {"id": 5, "title": 'English', "class_desc": 'Reinforce your language'},
]


STUDENT_CLASSES = [
    {"student_id": 1, "class_id": 1},
    {"student_id": 1, "class_id": 3},
    {"student_id": 1, "class_id": 5},
    {"student_id": 2, "class_id": 2},
    {"student_id": 2, "class_id": 4},
    {"student_id": 3, "class_id": 1},
    {"student_id": 3, "class_id": 2},
    {"student_id": 3, "class_id": 3},
    {"student_id": 3, "class_id": 4},
    {"student_id": 3, "class_id": 5},
    {"student_id": 4, "class_id": 2},
    {"student_id": 5, "class_id": 2},
    {"student_id": 5, "class_id": 3},
    {"student_id": 5, "class_id": 4},
    {"student_id": 6, "class_id": 5},
    {"student_id": 6, "class_id": 1}
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

for student in STUDENTS:
    new_student = Student(**student)
    session.add(new_student)

for db_class in CLASSES:
    new_class = Class(**db_class)
    session.add(new_class)

for student_class in STUDENT_CLASSES:
    student = session.query(Student).get(student_class["student_id"])
    db_class = session.query(Class).get(student_class["class_id"])
    student.classes.append(db_class)


session.commit()


print("*" * 10)

students = session.query(Student).all()

for student in students:
    if student.classes:
        for school_class in student.classes:
            print(student.first_name,
                  student.last_name,
                  school_class.title,
                  school_class.class_desc)

print("*" * 10)

school_classes = session.query(Class).all()

for school_class in school_classes:
    if school_class.students:
        for student in school_class.students:
            print(student.first_name,
                  student.last_name,
                  school_class.title,
                  school_class.class_desc)


session.close()

# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html

# In ORM Folder

# python3 -m many_to_many.main

# drop database relationships; create database relationships; use relationships;
