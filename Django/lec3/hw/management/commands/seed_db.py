from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from hw.models import *


class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding the database...'))
        

        user, user_created = (User.objects.
                         get_or_create(
                             username='admin',
                             defaults={
                                 'is_superuser': True, 'is_staff': True
                             }))
        user.set_password('123456')
        user.save()
        
        category, _ = Category.objects.get_or_create(name='Python')

        if user_created:
            author = Author.objects.create(user=user, birthday='1990-01-01')

            # post, _ = Post.objects.get_or_create(title="first post", defaults= {})



# python manage.py makemigrations hw --empty --name seed