from relationship_app.models import Author, Book, Library, Librarian


author = Author.objects.all()[2]
jk_rowlingbooks = Book.objects.filter(author_id=author)
print(jk_rowlingbooks) 

library = Library.objects.all()[0]
msa = Book.objects.filter(library=library)
print(msa) 

library1= Library.objects.all()[1]
librarian = Librarian.objects.filter(library_id=library1)
print(librarian)