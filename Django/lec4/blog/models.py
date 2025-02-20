from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    bio = models.TextField(blank=True, max_length=1000)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def username(self):
        return self.user.username 

    def __str__(self):
        return f'{self.user.username}'


from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from taggit.managers import TaggableManager

class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, validators=[
        MinLengthValidator(5),
        MaxLengthValidator(100), 
        RegexValidator(
            regex = '^[a-zA-Z].*$',
            message = "Title must start with a letter")
    ])
    text = models.TextField(
        validators=[
            MinLengthValidator(10)
        ]
    )
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.author.username}'