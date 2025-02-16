import django.core.validators as v
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Quote(models.Model):
    # props?
    author = models.CharField(max_length=40)
    quote = models.TextField()
    year = models.PositiveIntegerField()

    # administrative time stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} - {self.quote} - {self.year}"


# User is a built-in model


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[
        v.MinLengthValidator(2),
        v.MaxLengthValidator(100)
    ])
    description = models.TextField(blank=False, null=False)
    credits = models.PositiveSmallIntegerField(default=3,
                                               validators=[
                                                   v.MinValueValidator(1),
                                                   v.MaxValueValidator(5)
                                               ])

# student.courses
# course.students


class Student(models.Model):
    # relational fields
    birth_date = models.DateField()
    # student -> user (one-to-one)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.birth_date}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    grade = models.IntegerField(null=True,
                                validators=[
                                    v.MinValueValidator(0),
                                    v.MaxValueValidator(100)
                                ])

# student.enrollments