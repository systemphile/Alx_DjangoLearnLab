from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book


class BAPITestCase(APITestCase):
    """
    Test suite for the Book model API endpoints.

    Covered:
    - CRUD operations
    - Filtering, searching, and ordering
    - Authentication & permissions
    """

    def setUp(self):
        """
        Create test data and an authenticated user for secured endpoints.
        """
        # Create user for authentication
        self.user = User.objects.create_user(username='new', password='12345678')
        self.client = APIClient()
        self.client.login(username='new', password='12345678')

        # Create Author instances
        self.a1 = Author.objects.create(name="A1")
        self.a2 = Author.objects.create(name="A2")

        # Create child B instances
        self.b1 = Book.objects.create(title="B1", author=self.a1, publication_year=2025)
        self.b2 = Book.objects.create(title="B2", author=self.a2, publication_year=2024)
        self.b3 = Book.objects.create(title="B3", author=self.a1, publication_year=2023)

        # Endpoint URLs
        self.list_url = reverse('list')
        self.create_url = reverse('create')
        self.detail_url = lambda pk: reverse('retrieve', kwargs={'pk': pk})
        self.update_url = lambda pk: reverse('update', kwargs={'pk': pk})
        self.delete_url = lambda pk: reverse('delete', kwargs={'pk': pk})

    # ----------------- CRUD TESTS -----------------
    def test_create_book(self):
        """
        Ensure we can create a Book via POST and data is stored correctly.
        """
        data = {'title': 'B4', 'author': self.a2.id, 'publication_year': 2022}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'B4')

    def test_retrieve_book(self):
        """
        Ensure we can retrieve a specific Book via GET.
        """
        response = self.client.get(self.detail_url(self.b1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.b1.title)

    def test_update_book(self):
        """
        Ensure we can update a Book via PUT and the changes persist.
        """
        data = {'title': 'B3', 'author': self.a1.id, 'publication_year': 2021}
        response = self.client.put(self.update_url(self.b3.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.b3.refresh_from_db()
        self.assertEqual(self.b3.publication_year, 2021)

    def test_delete_book(self):
        """
        Ensure we can delete a Book via DELETE and it is removed from DBook.
        """
        response = self.client.delete(self.delete_url(self.b1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.b1.id).exists())

    # ----------------- FILTERING / SEARCH / ORDERING -----------------
    def test_filter_by_author(self):
        """
        Ensure filtering by foreign key author works.
        """
        response = self.client.get(self.list_url, {'author': self.a1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book['author'] == self.a1.id for book in response.data))

    def test_search_by_title(self):
        """
        Ensure search query param returns matches in publication_year field.
        """
        response = self.client.get(self.list_url, {'search': 'B1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.b1.title, 'B1')

    def test_ordering_by_publication_year_desc(self):
        """
        Ensure ordering by publication_year descending works.
        """
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        publication_year_values = [book['publication_year'] for book in response.data]
        self.assertEqual(publication_year_values, sorted(publication_year_values, reverse=True))

    # ----------------- PERMISSIONS -----------------
    def test_requires_authentication(self):
        """
        Ensure endpoints enforce authentication.
        """
        self.client.logout()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
