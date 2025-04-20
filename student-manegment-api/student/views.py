from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Students, Courses, Teachers, Enrollments, Grades
from .serializers import StudentSerializer, CourseSerializer, TeacherSerializer, EnrollmentSerializer, GradeSerializer

# View to list and create students
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

# View to list and create courses
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

# View to list and create teachers
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

# View to list and create enrollments
class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollments.objects.all()
    serializer_class = EnrollmentSerializer

# View to list and create grades
class GradeListCreateView(generics.ListCreateAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer
