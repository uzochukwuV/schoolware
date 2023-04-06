from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Index, name="login"),
    path("register/", views.Register, name="register"),
    path("role/<int:pk>/", views.Role, name="role"),
    path("profile/<int:pk>/", views.Profile, name="profile"),
    path("roles/", views.RoleList, name="roles"),
    path("courses/", views.CourseList, name="courses")
]
