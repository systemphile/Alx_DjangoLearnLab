from rest_framework import serializers
from .models import Book, Author
from datetime import date

# Serializer for Model Book.
# Purpose:
#   - Converts Book instances to/from JSON for API input/output.
#   - Enforces validation rules for the 'publication_year' field.
# Relationship Handling:
#   - The ForeignKey to Author is automatically handled by DRF using the 'author' field.
#   - When creating or updating a Book, clients can pass an Author's primary key for 'author'.
#   - The serializer will ensure that the provided Author exists.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    # Override the validate() method to apply custom validation rules
    # across multiple fields (in this case, only 'publication_year').
    # Runs after individual field validation and before saving.
    def validate(self, attrs):
        # Business rule: 'publication_year' must not be in the futur.
        if attrs.get('publication_year') > date.today().year:
            # The ValidationError accepts a dict to map the error to a specific field.
            raise serializers.ValidationError({
                'publication_year': 'Cannot be in the future.'
            })
        return attrs

# Serializer for Model Author.
# This simply serializes the fields of Author so they can be sent over the API.
# It also contains a nested serializer to the BookSerializer 
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
