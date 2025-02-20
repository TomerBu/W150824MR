from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import *
from .serializers import PostSerializer, CommentSerializer
from .models import Comment, Post
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class DemoViewSet(ViewSet):
    """
    Example empty viewset demonstrating the standard actions
    """
    def list(self, request):
       # posts = PostSerializer(Post.objects.all())
        return Response('list')
    def create(self, request):
        return Response('create')
    def retrieve(self, request, pk=None):
        return Response('retrieve')
    def update(self, request, pk=None):
        return Response('update')
    def partial_update(self, request, pk=None):
        return Response('partial_update')
    def destroy(self, request, pk=None):
        return Response('destroy')
class APIMap(APIView):
   """My Blog Map"""
   def get(self, request):
    return Response({
        "posts": reverse('posts', request=request),
        "post-details":  reverse('post-actions',kwargs = {"pk":1}, request=request),
    })


class PostsView2(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostActions2(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostsView(GenericAPIView, ListModelMixin ,CreateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        # use ListModelMixin's list method
        return self.list(request)
    
    def post(self, request):
        # use CreateModelMixin's create method
        return self.create(request)
    
class PostActions(GenericAPIView, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)