from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (SignUpView, 
                    profile_view, 
                    PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView, 
                    CommentUpdateView, 
                    CommentDeleteView, 
                    CommentCreateView, 
                    BlogPostDetailView)

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(template_name='blog/register.html'), name='register'),
    path('profile/', profile_view, name='profile'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='post-new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-confirm-delete'),
    path('post/<int:post_id>/comments', BlogPostDetailView.as_view(), name='comments'),
    path('post/<int:post_id>/comments/new', CommentCreateView.as_view(), name='comment_new'),
    path('post/<int:post_id>/comments/edit', CommentUpdateView.as_view(), name='comment_edit'),
    path('post/<int:post_id>/comments/delete', CommentDeleteView.as_view(), name='comment_delete'),
]