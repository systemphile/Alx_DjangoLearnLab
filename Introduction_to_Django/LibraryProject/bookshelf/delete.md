Steps for deleting the book created and confirming the deletion by trying to retrieve all books again.

```
>>> from bookshelf.models import Book
```
This command will import the Book Model

```
>>> book = Book.objects.get(title='Nineteen Eighty-Four')
```
Filter book by title 'Nineteen Eighty-Four' and save it into variable

```
>>> book.delete()
```

This command will delete the book instance from the model displaying the following output to confirm deletion:
```
(1, {'bookshelf.Book': 1})
```

Displaying final contents of the model after deletion:
```
>>> Book.objects.all().values()
<QuerySet []>
```