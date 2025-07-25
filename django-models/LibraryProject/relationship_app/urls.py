from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import list_books

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('list_books/', views.list_books, name='list_books'),
    path('library/', views.LibraryDetailView.as_view(template_name='relationship_app/library_detail.html'), name='library'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]