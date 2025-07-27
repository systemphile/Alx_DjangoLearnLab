### Step 1: Custom Permissions in Book Model

The Book model in bookshelf/models.py defines custom permissions:

```
class Book(models.Model):
    ...
    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
```

After defining permissions, run:

```
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Creating Groups and Assigning Permissions

In Django shell (python manage.py shell):

```
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

book_ct = ContentType.objects.get_for_model(Book)

# Create groups
viewers = Group.objects.create(name='Viewers')
editors = Group.objects.create(name='Editors')
admins = Group.objects.create(name='Admins')

# Assign permissions
view_perm = Permission.objects.get(codename='can_view', content_type=book_ct)
create_perm = Permission.objects.get(codename='can_create', content_type=book_ct)
edit_perm = Permission.objects.get(codename='can_edit', content_type=book_ct)
delete_perm = Permission.objects.get(codename='can_delete', content_type=book_ct)

viewers.permissions.set([view_perm])
editors.permissions.set([view_perm, create_perm, edit_perm])
admins.permissions.set([view_perm, create_perm, edit_perm, delete_perm])
```

### Step 3: Enforcing Permissions in Views

In bookshelf/views.py, use decorators:

```
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    ...

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    ...

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    ...

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    ...
```

### Step 4: Manual Testing Instructions

Create user accounts via Django admin or createsuperuser.

Assign users to Viewers, Editors, or Admins groups.

Log in as different users and try accessing the views protected by permissions.

Confirm that access is granted or denied appropriately.