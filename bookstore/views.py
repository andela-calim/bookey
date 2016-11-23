from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Book, Category


# Create your views here.


class HomePageView(View):
    def get(self, request):
        """
        Renders Home View with data
        """
        books = Book.objects.all()
        categories = Category.objects.all()
        search_query = None

        q = request.GET.get('q')
        c = request.GET.get('c')

        if q:
            books = books.filter(title__icontains=q)
            search_query = q
        elif c:
            category = get_object_or_404(Category, pk=c)
            books = books.filter(category=category)
            search_query = c

        context = {
            'books': books,
            'categories': categories,
            'search_query': search_query
        }

        return render(request, 'bookstore/home.html', context)