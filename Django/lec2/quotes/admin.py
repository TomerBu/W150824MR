from django.contrib import admin

# Register your models here.
from .models import Quote, Student, Course, Enrollment

admin.site.register([Quote, Student, Course, Enrollment])

# python manage.py makemigrations quotes
# python manage.py migrate