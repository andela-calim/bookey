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

        q = request.GET.get('q')
        c = request.GET.get('c')

        if q:
            books = books.filter(title__icontains=q)
        elif c:
            category = get_object_or_404(Category, pk=c)
            books = books.filter(category=category)

        context = {
            'books': books
        }

        return render(request, 'bookstore/home.html', context)