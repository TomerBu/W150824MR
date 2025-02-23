from .serializers import *
from .models import Comment, Post, UserProfile, PostUserLikes
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        reply_to = data.get('reply_to')
        post_id = data.get('post')
        
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


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class LikesViewSet(ModelViewSet):
    queryset = PostUserLikes.objects.all()
    serializer_class = PostUserLikesSerializer
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
