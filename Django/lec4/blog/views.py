from core.utils import try_parse_int

from .serializers import *
from .models import Comment, Post, UserProfile, PostUserLikes
from rest_framework.response import Response

from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from core.permissions import IsOwnerOrModelPermissions

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

from rest_framework.reverse import reverse

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout
from rest_framework.authtoken.serializers import AuthTokenSerializer

from core.authentication import get_tokens_for_user
class AuthViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail = False, methods=['post', 'get'])
    def login(self, request):
        serializer = AuthTokenSerializer(data=request.data, context = {'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        # from core.authentication import get_tokens_for_user
        jwt = get_tokens_for_user(user)
        login(request, user)
        return Response({"token": token.key, 'jwt': jwt})
   
    @action(detail = False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        try:
            logout(request)
            request.user.auth_token.delete()
        except:
            pass

        return Response({"message": "Logged out successfully"})



    def list(self, request):
        return Response({
            "login":reverse('auth-login', request=request),
            "register": reverse('auth-register', request=request),
            "logout": reverse('auth-logout', request=request),
        })
    
    @action(detail = False, methods=['post', 'get'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        jwt = get_tokens_for_user(user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'jwt':jwt})


    #from rest_framework.authtoken.serializers import AuthTokenSerializer



class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrModelPermissions]


    def create(self, request, *args, **kwargs):
        data = request.data
        reply_to = data.get('reply_to')
        post_id = try_parse_int(data.get('post'))
        
        if reply_to:
            replied = Comment.objects.get(id=reply_to)
            print(replied)
            if (
                replied and replied.post.id != post_id
            ):
                return Response(
                    {"error": "Reply must be on the same post"},
                    status=400
                )

        return super().create(request, *args, **kwargs)

    # build a tree structure of comments

    def list(self, request, *args, **kwargs):
        """Builds a nested comment structure"""
        res = super().list(request, *args, **kwargs)

        comments = res.data
        comments_dict = {comment["id"]: comment for comment in comments}
        root_comments = []

        for comment in comments:
            parent_id = comment['reply_to']
            if parent_id is None:
                root_comments.append(comment)
            else:
                parent = comments_dict.get(parent_id)
                if parent:
                    if "replies" not in parent:
                        parent["replies"] = []
                    parent["replies"].append(comment)

        res.data = root_comments
        return res


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrModelPermissions]


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrModelPermissions]
  


class LikesViewSet(ModelViewSet):
    queryset = PostUserLikes.objects.all()
    serializer_class = PostUserLikesSerializer
    permission_classes = [IsOwnerOrModelPermissions]
# class DemoViewSet(ViewSet):
#     """
#     Example empty viewset demonstrating the standard actions
#     """
#     def list(self, request):
#        # posts = PostSerializer(Post.objects.all())
#         return Response('list')
#     def create(self, request):
#         return Response('create')
#     def retrieve(self, request, pk=None):
#         return Response('retrieve')
#     def update(self, request, pk=None):
#         return Response('update')
#     def partial_update(self, request, pk=None):
#         return Response('partial_update')
#     def destroy(self, request, pk=None):
#         return Response('destroy')
# class APIMap(APIView):
#    """My Blog Map"""
#    def get(self, request):
#     return Response({
#         "posts": reverse('posts', request=request),
#         "post-details":  reverse('post-actions',kwargs = {"pk":1}, request=request),
#     })


# class PostsView2(ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

# class PostActions2(RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

# class PostsView(GenericAPIView, ListModelMixin ,CreateModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request):
#         # use ListModelMixin's list method
#         return self.list(request)

#     def post(self, request):
#         # use CreateModelMixin's create method
#         return self.create(request)

# class PostActions(GenericAPIView, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk)
