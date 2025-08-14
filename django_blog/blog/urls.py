from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, profile_view, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(template_name='register.html'), name='register'),
    path('profile/', profile_view, name='profile'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='post-new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]