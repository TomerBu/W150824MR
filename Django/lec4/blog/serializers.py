from .models import Post, Comment, UserProfile, PostUserLikes
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class PostUserLikesSerializer(ModelSerializer):
    class Meta:
        model = PostUserLikes
        fields = '__all__'