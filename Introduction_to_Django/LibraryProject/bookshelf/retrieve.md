Retrieve and display all attributes of the book we just created.

```
>>> from bookshelf.models import Book
```
This command will import the Book Model

```
>>> Book.objects.get(title="1994")
```

If the model contains data, the expected output is as follows:
```
<Book: Book object (1)>
```