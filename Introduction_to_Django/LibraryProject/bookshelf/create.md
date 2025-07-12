Steps for creating a new instance of our model

```
>>> from bookshelf.models import Book
```
This command will import the Book model

```
>>> book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
```
We use the model to initialize a new Book instance using its defined attributes.

```
>>> book.save()
```
Save the new book instance to the model