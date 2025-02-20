from django.contrib import admin

from hw.models import FunFact

# Register your models here.

admin.site.register([FunFact])


# python manage.py createsuperuser