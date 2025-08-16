from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from taggit.forms import TagWidget

custom_tag_widget = TagWidget()
custom_tag_widget.attrs['placeholder'] = 'Add tags separated by commas'

class RegistrationForm(UserCreationForm):
    # additional fields
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()

    # include Meta class
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'tags']
        widgets = widgets = {
            'tags': custom_tag_widget  # TagWidget() explicitly used
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None) #store logged-in user
        super().__init__(*args, **kwargs)
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError('Title must be at least 3 characters long')
        return title
    
    def save(self, commit = True):
        instance = super().save(commit=False)
        if self.user:
            instance.author = self.user #set logged in user as the author
        if commit:
            instance.save()
        return instance
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your comment here...'
            }),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content.strip():
            raise forms.ValidationError("Comment cannot be empty.")
        return content