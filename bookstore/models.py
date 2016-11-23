from django.db import models


# Create your models here.
class Category(models.Model):
    """
    Category Model
    """
    name = models.CharField(max_length=200)


class Book(models.Model):
    """
    Book Model
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    is_hardcover = models.BooleanField(default=False)

