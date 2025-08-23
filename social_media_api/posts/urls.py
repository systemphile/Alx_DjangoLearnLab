from rest_framework.routers import DefaultRouter
from rest_framework.urls import path
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments',CommentViewSet)

urlpatterns = [] + router.urls