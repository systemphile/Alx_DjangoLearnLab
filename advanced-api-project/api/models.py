from django.db import models

# Create your models here.
from django.db import models

# Model Author represents the parent entity in our example.
# Think of it as a category, group, or any container for multiple Book objects.
# Other models (like Book) will hold a ForeignKey to Author.
class Author(models.Model):
    name = models.CharField(max_length=200)

# Model Book represents the child entity in the Author–Book relationship.
# Each Book is linked to exactly one Author (via ForeignKey).
# This creates a one-to-many relationship: one Author can have many Books.
class Book(models.Model):
    title = models.CharField(max_length=200)

    # Field publication_year is the value we want to validate in the serializer
    publication_year = models.IntegerField()

    # ForeignKey to Author establishes the parent-child relationship.
    # related_name='books' allows reverse lookup from Author: author_instance.books.all()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')