from django.contrib import admin

from .models import Students, Course

admin.site.register(Course)
admin.site.register(Students)