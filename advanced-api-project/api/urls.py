from rest_framework.urls import path
from .views import BookCreateView, BookListView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='list'),
    path('books/create/', BookCreateView.as_view(), name='create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='retrieve'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='delete'),
]