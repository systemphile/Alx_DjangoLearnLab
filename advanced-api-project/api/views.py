from rest_framework import generics, permissions, serializers
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.

# Create View with custom validation & permission check
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer(queryset)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # only logged-in users can create

    def perform_create(self, serializer):
        # Add extra logic before saving
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title__iexact=title).exists():
            raise serializers.ValidationError({"title": "Book with this title already exists."})

        serializer.save()  # Save if no validation errors

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer(queryset)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer(queryset)
    permission_classes = [permissions.IsAuthenticated] # only logged-in users can create

# Update View with permission & filtering
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Optional filter: user can only update books with published_year >= 2025
        return super().get_queryset().filter(published_year__gte=2025)

    def perform_update(self, serializer):
        # Example of extra business logic before updating
        if serializer.validated_data.get('title') == "Forbidden Title":
            raise serializers.ValidationError({"title": "This title is not allowed."})

        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]