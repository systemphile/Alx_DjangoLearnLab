from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, profile_view

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html', name='login')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(template_name='blog/signup.html'), name='register'),
    path('profile/', profile_view(), name='profile'),
]