from django.contrib import admin
from .models import Book, Author
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django import forms
from bookshelf.models import CustomUser

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    list_filter = ('title',)
    search_fields = ('title', 'author')

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