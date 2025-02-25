from .models import Post, Comment, UserProfile, PostUserLikes

from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from rest_framework.serializers import HiddenField, SerializerMethodField

from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': False, 'required': True},
            'id': {'read_only': True},
            'email': {'required': True},
            'username': {'required': True, 'min_length':3},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    # TODO: update will not encrypt the password




class TagField(TagListSerializerField):

    def to_internal_value(self, value):
        request = self.context.get('request')

        is_browsable_api = (
            request
            and hasattr(request, 'accepted_renderer')
            and request.accepted_renderer.format == 'api'
        )
        
        if (
            is_browsable_api
            and isinstance(value, list)
            and len(value) == 1
            and isinstance(value[0], str)
        ):
            value = value[0].split() #by default splits by space

        return super().to_internal_value(value)


class CurrentUserDefault():
    requires_context = True

    def __call__(self, serializer_field):
        request =  serializer_field.context['request']
        return request.user.userprofile

   
class PostSerializer(TaggitSerializer, ModelSerializer):
    tags = TagField(style={'base_template': 'textarea.html'})  
    author = HiddenField(default = CurrentUserDefault())
    author_id = SerializerMethodField()
    
    class Meta:
        model = Post
        fields = '__all__'

    def get_author_id(self, obj):
        return obj.author.id

class CommentSerializer(ModelSerializer):
    author = HiddenField(default = CurrentUserDefault())
    author_id = SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = '__all__'

    def get_author_id(self, obj):
        return obj.author.id

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PostUserLikesSerializer(ModelSerializer):
    class Meta:
        model = PostUserLikes
        fields = '__all__'
