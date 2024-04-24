from django.shortcuts import render

from books.models import BookModel


def home_view(request):
    books = BookModel.objects.all()
    context = {
        'books_list': books
    }
    return render(request, 'home.html', context)