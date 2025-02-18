from django.db import migrations
from django.core.management import call_command

class Migration(migrations.Migration):

    def run_seed(apps, schema_editor):
        call_command('seed_db')

    dependencies = [
        ('hw', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(run_seed),
    ]

# python manage.py migrate hw