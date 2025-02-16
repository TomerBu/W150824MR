from django.core.management.base import BaseCommand

from django.contrib.auth.models import User, Group, Permission
from quotes.models import Quote, Student, Course, Enrollment


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding the database...')

        quote, is_created = Quote.objects.get_or_create(quote='Scripttt!', defaults={
            'author': 'Itamar',
            'year': 2024
        })

        user, _ = User.objects.get_or_create(username='itamar', defaults={
            'first_name': 'Itamar',
        })

        user.set_password('123456')
        user.save()

        student, _ = (
            Student.objects
            .get_or_create(
                user=user, defaults={'birth_date': '1980-01-01'}
            )
        )


# run the command:
# python manage.py seed_db
