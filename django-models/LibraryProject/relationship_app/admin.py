from django.contrib import admin
from relationship_app.models import Book, Author, Library, Librarian, UserProfile

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author',)
    list_filter = ('title','author',)
    search_fields = ('title',)
admin.site.register(Book, BookAdmin)

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name','books',)
    search_fields = ('name',)
admin.site.register(Library, LibraryAdmin)

class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
admin.site.register(Librarian, LibrarianAdmin)

admin.site.register(UserProfile)