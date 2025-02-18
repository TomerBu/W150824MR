from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)

class Kitten(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)

# python manage.py makemigrations api
# python manage.py migrate