from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, profile_view, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(template_name='register.html'), name='register'),
    path('profile/', profile_view, name='profile'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/new/', PostCreateView.as_view(), name='posts-new'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='posts-edit'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='posts-delete'),
]