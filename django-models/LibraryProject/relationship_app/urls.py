from django.urls import path
from . import views

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('library/', views.LibraryDetailView.as_view, name='library'),
]