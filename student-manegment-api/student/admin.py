from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Students, Teachers

# Register your models here
admin.site.register(Students)
admin.site.register(Teachers)
