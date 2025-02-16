from django.db import models

# Create your models here.
class Quote(models.Model):
    # props?
    author = models.CharField(max_length=40)
    quote = models.TextField()
    year = models.IntegerField()

    # administrative time stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} - {self.quote} - {self.year}"