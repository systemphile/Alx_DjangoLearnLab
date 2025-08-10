# Authentication and Permissions in the Project

## Authentication

This project uses **Token-Based Authentication** provided by Django REST Framework.

### Setup Steps:
1. Enabled token auth via `rest_framework.authtoken` in `INSTALLED_APPS`
2. Ran `python manage.py migrate` to create token tables
3. Configured `TokenAuthentication` in `REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']`
4. Added a login endpoint at `/login/` using `obtain_auth_token` to issue tokens

## Permissions

Most views require the user to be authenticated.

- Used `IsAuthenticated` to protect sensitive endpoints like `/books_all/`
- You can create custom permission classes if more control is needed

### Example Curl Command

```bash
curl -X POST http://localhost:8000/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_user", "password": "your_pass"}'
```

Use the returned token to access protected views:

```bash
curl http://localhost:8000/books_all/ \
  -H "Authorization: Token your_token_here"
  ```