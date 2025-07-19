from relationship_app.models import Author, Book, Library, Librarian

author_name = Author.objects.get(name='J.K. Rowling')
author = Author.objects.get(name=author_name)
jk_rowlingbooks = Book.objects.filter(author=author)
print(jk_rowlingbooks)

library_name = Library.objects.all()[0]
library = Library.objects.get(name=library_name)
library.books.all()

library1= Library.objects.all()[1]
librarian = Librarian.objects.filter(library_id=library1)
print(librarian)