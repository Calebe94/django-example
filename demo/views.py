from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

class Another(View):
    books = Book.objects.all()
    # books = Book.objects.filter(is_published=True)
    # books = Book.objects.get(id=2)
    # output = "We have this book {}".format(books.title )
    output = "We have {} books in DB<br>".format(len(books))
    output += "And they are:<br>"
    for book in books:
        output += "* {} - {} - {} - {}<br>".format(book.id, book.title, book.description, book.price)

    def get(self, request):
        return HttpResponse(self.output)
