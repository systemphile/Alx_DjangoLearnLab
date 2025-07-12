Steps for retrieving and displaying all attributes of the book we just created.

```
>>> from bookshelf.models import Book
```
This command will import the Book Model

```
>>> Book.objects.all().values()
```
An empty Query set is displayed if the model is empty

```
<QuerySet []>
```

If the model contains data, the expected output is as follows:
```
>>> Book.objects.all().values()
<QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>
```

Note that the 'id' field is automatically assigned.