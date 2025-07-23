from flask import Blueprint, request, jsonify
from app.controllers import student_controller, attendance_controller
from app.extensions.db import db
# from app.routes.routing import app_blueprint

# app_blueprint = Blueprint("app_blueprint", __name__)
app_blueprint = Blueprint('app', __name__)

# Student Routes
@app_blueprint.route('/add_student', methods=['POST'])
def add_student():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        student = student_controller.create_student(data)

        return jsonify({
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'roll_no': student.roll_no
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app_blueprint.route('/update_student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    student = student_controller.update_student(student_id, data)
    if student:
        return jsonify({'id': student.id, 'name': student.name, 'email': student.email, 'roll_no': student.roll_no})
    return jsonify({'error': 'Student not found'}), 404



# @app_blueprint.route('/update_student/<int:student_id>', methods=['PUT'])
# def update_student(student_id):
#     data = request.json

#     student = student.query.get(student_id)
#     if not student:
#         return jsonify({'error': 'Student not found'}), 404

#     # Update fields if provided
#     if 'name' in data:
#         student.name = data['name']
#     if 'email' in data:
#         student.email = data['email']
#     if 'roll_no' in data:
#         student.roll_no = data['roll_no']

#     db.session.commit()

#     return jsonify({
#         'id': student.id,
#         'name': student.name,
#         'email': student.email,
#         'roll_no': student.roll_no
#     }), 200

@app_blueprint.route('/student', methods=['GET'])
def get_students():
    students = student_controller.get_students()
    return jsonify([{'id': s.id, 'name': s.name, 'email': s.email, 'roll_no': s.roll_no} for s in students])


# Attendance Routes
@app_blueprint.route('/attendance', methods=['POST'])
def add_attendance():
    data = request.json
    record = attendance_controller.create_attendance(data)
    return jsonify({'id': record.id, 'student_id': record.student_id, 'date': record.date, 'status': record.status})

@app_blueprint.route('/attendance/<int:attendance_id>', methods=['PUT'])
def update_attendance(attendance_id):
    data = request.json
    record = attendance_controller.update_attendance(attendance_id, data)
    if record:
        return jsonify({'id': record.id, 'student_id': record.student_id, 'date': record.date, 'status': record.status})
    return jsonify({'error': 'Record not found'}), 404

@app_blueprint.route('/attendance', methods=['GET'])
def get_attendance():
    records = attendance_controller.get_attendance()
    return jsonify([{
        'id': r.id, 'student_id': r.student_id, 'date': r.date, 'status': r.status
    } for r in records])
