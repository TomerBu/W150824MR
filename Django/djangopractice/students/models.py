from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

#python3 manage.py makemigrations students
#python manage.py migrate 
#python manage.py createsuperuser