from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics, permissions

from .models import Post, Comment
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