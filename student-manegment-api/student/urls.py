from django.urls import path
from .views import StudentListCreateView, CourseListCreateView, TeacherListCreateView, EnrollmentListCreateView, GradeListCreateView

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
    path('grades/', GradeListCreateView.as_view(), name='grade-list-create'),
]
