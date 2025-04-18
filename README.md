# Django REST Framework API Documentation Setup using drf-yasg

This guide walks you through setting up API documentation for your Django REST Framework application using drf-yasg, which provides a Swagger UI for easy, interactive documentation.

## Steps to Set Up

### Step 1: Install the Required Package

First, you need to install `drf-yasg`. You can do this using pip:

```bash
pip install drf-yasg

```
---
INSTALLED_APPS = [
    # Other apps
    'drf_yasg',
]

---
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include

schema_view = get_schema_view(
   openapi.Info(
      title="Student Management API",
      default_version='v1',
      description="API documentation for the Student Management system",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@studentmanagement.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('your_app.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
]


---

http://localhost:8000/docs/


---



from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers

class StudentSearchSerializer(serializers.Serializer):
    name = serializers.CharField()

class StudentSearch(APIView):
    @swagger_auto_schema(request_body=StudentSearchSerializer, responses={200: StudentSerializer(many=True)})
    def post(self, request):
        name = request.data.get('name')
        students = Student.objects.filter(name__icontains=name)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


---


This is your complete `README.md` file. You can copy and save this as a `.md` file in your project directory. Let me know if you need further adjustments!
