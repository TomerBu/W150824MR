from django.db import models

# Create your models here.
"""
FunFact:
תכונות:
text, source, source_url, language, permalink
"""


class FunFact(models.Model):
    text = models.TextField()
    source = models.CharField(max_length=100)
    source_url = models.URLField()
    language = models.CharField(
        max_length=2,
        choices=[('he', 'Hebrew'), ('en', 'English')]
    )

    def __str__(self):
        return self.text

# python manage.py makemigrations hw
# python manage.py migrate