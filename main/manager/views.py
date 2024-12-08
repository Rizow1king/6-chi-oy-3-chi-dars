from django.shortcuts import render
from .models import Course, Students
from django.core.handlers.wsgi import WSGIRequest


def home(request: WSGIRequest):
    courses = Course.objects.all()
    students = Students.objects.all()
    return render(request, 'index.html', {'courses': courses, 'students': students})
