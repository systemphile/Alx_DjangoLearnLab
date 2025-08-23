from rest_framework.routers import DefaultRouter
from rest_framework.urls import path
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments',CommentViewSet)

urlpatterns = [
    path('feed/', FeedView.as_view(), name='user-feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
] + router.urls