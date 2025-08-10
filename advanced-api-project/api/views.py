from rest_framework import generics, serializers, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
import django_filters
from django_filters import rest_framework


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains') # case-insensitive partial match
    
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

# Create View with custom validation & permission check
class BookListView(generics.ListAPIView):
    """
    API endpoint to retrieve a list of B instances with:
    - Filtering by specific fields
    - Text search on chosen fields
    - Ordering by allowed fields

    Filtering:
        ?publication_year=value          (exact or partial if icontains is used)
        ?author=1              (filter by foreign key Author's ID)
        ?publication_year=value&author=1      (combine filters)

    Searching:
        ?search=text      (searches in publication_year and related Author.name)

    Ordering:
        ?ordering=publication_year       (ascending order by publication_year)
        ?ordering=-publication_year      (descending order by publication_year)
        ?ordering=author,-publication_year    (order by A ID ascending, then publication_year descending)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer(queryset)
    permission_classes = [IsAuthenticatedOrReadOnly] # only logged-in users can create

     # Backends for filtering, search, and ordering
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_class = BookFilter

    # Search configuration
    search_fields = ['title', 'author__name']

    # Allow ordering by these fields
    ordering_fields = ['title', 'title',]

    # Default ordering (optional)
    ordering = ['id']

    def perform_create(self, serializer):
        # Add extra logic before saving
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title__iexact=title).exists():
            raise serializers.ValidationError({"title": "Book with this title already exists."})

        serializer.save()  # Save if no validation errors

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer(queryset)
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer(queryset)
    permission_classes = [IsAuthenticated] # only logged-in users can create

# Update View with permission & filtering
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]