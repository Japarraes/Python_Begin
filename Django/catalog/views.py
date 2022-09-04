from ast import Num
from django.shortcuts import render

# Create your views here.
from .models import Author, Book, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_author = Author.objects.all().count()
    disponibles = BookInstance.objects.filter(status__exact='a').count()

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_author': num_author,
            'num_instances': num_instances,
            'disponibles': disponibles
        }
    )

