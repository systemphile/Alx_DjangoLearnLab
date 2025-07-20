from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('list_books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view, name='library'),
]