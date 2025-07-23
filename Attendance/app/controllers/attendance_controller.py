from app.extensions import db
from app.models.models import Attendance

def create_attendance(data):
    attendance = Attendance(
        student_id=data['student_id'],
        date=data['date'],
        status=data['status']
    )
    db.session.add(attendance)
    db.session.commit()
    return attendance

def update_attendance(attendance_id, data):
    record = Attendance.query.get(attendance_id)
    if not record:
        return None
    for key in data:
        setattr(record, key, data[key])
    db.session.commit()
    return record

def get_attendance():
    return Attendance.query.all()
