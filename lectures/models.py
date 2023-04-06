from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.

TITLE_CHOICES = [
    ("MR", "Mr."),
    ("MRS", "Mrs."),
    ("MS", "Ms.")
]


class User(AbstractUser):

    email = models.EmailField(_("email address"), unique=True)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    courses_handled = models.ForeignKey(
        "Courses", verbose_name=("User"), on_delete=models.CASCADE, null=True, blank=True)
    faculty = models.ForeignKey("Faculty", verbose_name=(
        "faculty"), on_delete=models.CASCADE, blank=True, null=True)
    phone_no = models.CharField(
        max_length=50, blank=True, null=True, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "last_name", "first_name"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})


class Faculty(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    head = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})


class Courses(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    faculty = models.ForeignKey("Faculty", verbose_name=(
        "faculty"), on_delete=models.CASCADE)
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "course"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"pk": self.pk})


class Department(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "department"
        verbose_name_plural = "department"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dep_detail", kwargs={"pk": self.pk})


class Roles(models.Model):
    User = models.ForeignKey("User", verbose_name=(
        "User"), on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey("Courses", verbose_name=(
        "course"), on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "role"
        verbose_name_plural = "roles"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("role_detail", kwargs={"pk": self.pk})
