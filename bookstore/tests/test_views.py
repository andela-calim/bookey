from django.test import TestCase, Client
from django.urls import reverse

from ..models import Category, Book


class HomePageViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        """
        Create different categories
        """
        self.fiction_category = Category.objects.create(name="Fiction")
        self.gothic_category = Category.objects.create(name="Gothic")
        self.adventure_category = Category.objects.create(name="Adventure")

        """
        Create three books
        """
        self.book1 = Book.objects.create(
            title="Harry Potter",
            author="J.K. Rowlings",
            category=self.fiction_category,
            description="There lived a boy...",
            is_hardcover=True
        )
        self.book2 = Book.objects.create(
            title="The Bourne Supremacy",
            author="Jason Bourne",
            category=self.adventure_category
        )
        self.book3 = Book.objects.create(
            title="The Spread",
            author="Random Guy",
            category=self.fiction_category
        )

    def test_home_view_returns_success(self):
        response = self.client.get(reverse('bookstore:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_search_by_book_title(self):
        search_query = 'harry'
        response = self.client.get('{}?q={}'.format(reverse('bookstore:home'), search_query))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['books'].count(), 1)
        self.assertEqual(response.context['books'].first(), self.book1)

        search_query = 'the'
        response = self.client.get('{}?q={}'.format(reverse('bookstore:home'), search_query))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['books'].count(), 2)

