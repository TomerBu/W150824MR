from taggit.managers import TaggableManager
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
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


STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('archived', 'Archived')
]

class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, validators=[
        MinLengthValidator(5),
        MaxLengthValidator(100),
        RegexValidator(
            regex='^[a-zA-Z].*$',
            message="Title must start with a letter")
    ])
    text = models.TextField(
        validators=[
            MinLengthValidator(10)
        ]
    )
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft"
    )

    def __str__(self):
        return f'{self.title} by {self.author.username}'


class Comment(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(
        validators = [MinLengthValidator(2)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reply_to = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True
    )
    def __str__(self):
        return f'{self.text} by {self.author.username}'


# user may like many posts
# post may be liked by many users
# many to many with extra fields


LIKE_CHOICES = [
    ('like', 'Like'),
    ('dislike', 'Dislike')
]

class PostUserLikes(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_type = models.CharField(
        choices=LIKE_CHOICES,
        max_length=10,
        default='like'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # prevent multiple likes/dislikes per post
    class Meta:
        unique_together = ['user', 'post']
        #db_table = "music_album"
        # https://docs.djangoproject.com/en/5.1/ref/models/options/

    def __str__(self):
        return f'{self.user.username} {self.like_type}d {self.post.title}'

# INSTALLED_APPS += ['taggit', 'blog']
# pip install Pillow
# python manage.py makemigrations blog
# python manage.py migrate
# 
# python manage.py runserver