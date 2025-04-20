from rest_framework import serializers
from .models import Students, Courses, Teachers, Enrollments, Grades

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = [ 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = [ 'course_name', 'course_description', 'course_duration']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = [ 'first_name', 'last_name', 'email', 'phone_number', 'address']

class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = Enrollments
        fields = [ 'student', 'course', 'enrollment_date']

class GradeSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = Grades
        fields = ['student', 'course', 'grade', 'date_assigned']
