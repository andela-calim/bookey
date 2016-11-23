from django.shortcuts import render
from django.views import View

from .models import Book

# Create your views here.


class HomePageView(View):
    def get(self, request):
        """

        :param request:
        :return:
        """
        books = Book.objects.all()

        q = request.GET.get('q')

        if q:
            books = books.filter(title__icontains=q)

        context = {
            'books': books
        }

        return render(request, 'bookstore/home.html', context)