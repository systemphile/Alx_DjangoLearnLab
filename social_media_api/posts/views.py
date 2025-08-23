from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

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