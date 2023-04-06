from django.shortcuts import render
from .models import Courses, User, Faculty, Department

# Create your views here.


def Index(request):
    return render(request, "signup.html")


def Register(request):
    return render(request, "register.html")


def Role(request):
    return render(request, "role.html")


def Profile(request):
    return render(request, "profile.html")


def CourseList(request):
    return render(request, "all_courses.html")


def RoleList(request):
    return render(request, "all_roles.html")
