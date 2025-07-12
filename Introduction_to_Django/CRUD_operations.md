### 1. Create a new instance of our model

#### Command
```
>>> from bookshelf.models import Book
>>> book = Book(title='1984', author='George Orwell', publication_year=1949)
>>> book.save()
```

### 2. Retrieve and display all attributes of the book we just created.

#### Command
```
>>> Book.objects.all().values()
```

#### Expected outcome
```
<QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>
```

### 3. Update the title of “1984” to “Nineteen Eighty-Four” and saving the changes.

#### Command
```
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title='1984')
>>> book.title = 'Nineteen Eighty-Four'
>>> book.save()
>>> book.title
```
#### Expected outcome
```
'Nineteen Eighty-Four'
```

### 4. delete the book created and confirm the deletion by trying to retrieve all books again.

#### Command
```
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title='Nineteen Eighty-Four')
>>> book.delete()
```

#### Expected outcome
```
(1, {'bookshelf.Book': 1})
```

Displaying final contents of the model after deletion:
```
>>> Book.objects.all().values()
<QuerySet []>
```