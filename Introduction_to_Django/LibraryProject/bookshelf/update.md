Steps for Updating the title of “1984” to “Nineteen Eighty-Four” and saving the changes.

```
>>> from bookshelf.models import Book
```
This command will import the Book Model

```
>>> book = Book.objects.get(title='1984')
```
Filter book by title '1984' and save it into a new variable

```
>>> book.title
'1984'
```

This command will access the current book title. To update the book to 'Nineteen Eighty-Four', we run the following commands:
```
>>> book.title = 'Nineteen Eighty-Four'
>>> book.save()
```

Display updated title
```
>>> book.title
'Nineteen Eighty-Four'
```