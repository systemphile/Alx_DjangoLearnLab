from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = IsOwnerOrReadOnly
    filter_backends = [DjangoFilterBackend, SearchFilter]
    
    # Option 1: Exact filtering (if you want ?title=hello)
    filterset_fields = ["title", "content"]

    # Option 2: Search filtering (?search=keyword looks in both fields)
    search_fields = ["title", "content"]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes =IsOwnerOrReadOnly

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get all users the current user follows
        following_users = user.following.all()
        # Return posts by those users, ordered newest first
        return Post.objects.filter(author__in=following_users).order_by("-created_at")
    
class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        # Prevent duplicate likes
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"error": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(user=request.user, post=post)
        return Response({"success": f"You liked '{post.title}'"}, status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({"error": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"success": f"You unliked '{post.title}'"}, status=status.HTTP_200_OK)