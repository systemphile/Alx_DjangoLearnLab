from django.contrib import admin
from relationship_app.models import Book, Author, Library, Librarian, UserProfile, CustomUser
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django import forms

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

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)