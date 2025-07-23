# from app import db
from app.models.models import Student
from app.extensions.db import db
from app.models.models import Student

def create_student(data):
    student = Student(name=data['name'], email=data.get('email'), roll_no=data['roll_no'])
    db.session.add(student)
    db.session.commit()
    return student

def update_student(student_id, data):
    student = Student.query.get(student_id)
    if not student:
        return None
    for key in data:
        setattr(student, key, data[key])
    db.session.commit()
    return student

def get_students():
    return Student.query.all()
