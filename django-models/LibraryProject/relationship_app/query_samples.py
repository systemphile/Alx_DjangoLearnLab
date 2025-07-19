from relationship_app.models import Author, Book, Library, Librarian


author = Author.objects.all()[2]
jk_rowlingbooks = author.book_set.all()
print(jk_rowlingbooks) 

library_name = Library.objects.all()[0]
library = Library.objects.get(name=library_name)
library.books.all()

library1= Library.objects.all()[1]
librarian = Librarian.objects.filter(library_id=library1)
print(librarian)