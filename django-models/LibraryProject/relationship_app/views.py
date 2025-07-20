from django.shortcuts import render
from relationship_app.models import Author, Book, Library, Librarian
from django.views.generic import DetailView, ListView

# Create your views here.    
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'templates/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'templates/library_detail.html'
    context_object_name = 'library'