from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView

# Create your views here.    
def list_books(request):
    books = Book.objects.all()
    template_name = 'relationship_app/list_books.html'
    context = {
        'books': books
    }
    return render(request, template_name=template_name, context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'