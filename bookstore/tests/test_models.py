from django.db import IntegrityError
from django.test import TestCase
from ..models import Category, Book


# Create your tests here.
class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Fiction")

    def test_category_instance(self):
        self.assertIsInstance(self.category, Category)


class BookModelTest(TestCase):
    def setUp(self):
        self.adventure_category = Category.objects.create(name="Adventure")
        self.fiction_category = Category.objects.create(name="Fiction")

        self.book = Book.objects.create(
            title="Alice in Wonderland",
            author="Chiemeka Aubrey",
            category=self.adventure_category
        )

    def test_book_instance(self):
        self.assertIsInstance(self.book, Book)

    def test_title_field_is_required(self):
        self.book = Book()
        self.book.title = None
        self.book.author = "Aubrey Alim"
        self.book.category = self.adventure_category

        with self.assertRaises(IntegrityError):
            self.book.save()
