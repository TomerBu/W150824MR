from .models import Post, Comment, UserProfile, PostUserLikes
from rest_framework.serializers import ModelSerializer
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


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

class PostSerializer(TaggitSerializer, ModelSerializer):
    tags = TagField(style={'base_template': 'textarea.html'})  

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
