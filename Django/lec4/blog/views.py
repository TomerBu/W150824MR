from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import *
from .serializers import PostSerializer
from .models import *

from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
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