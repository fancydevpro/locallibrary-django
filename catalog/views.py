from django.shortcuts import render

# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre

def index(request):
  num_books = Book.objects.all().count()
  num_instances = BookInstance.objects.all().count()

  num_instances_available = BookInstance.objects.filter(status__exact='a').count()

  num_authors = Author.objects.count()

  num_books_includes_book = Book.objects.filter(title__icontains='book').count()
  num_genres_romance = Genre.objects.filter(name__exact='romance').count()

  context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
    'num_books_includes_book': num_books_includes_book,
    'num_genres_romance': num_genres_romance,
  }

  return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
  model = Book

  '''def get_queryset(self):
    return Book.objects.filter(title__icontains='book')[:5]
  
  def get_context_data(self, **kwargs):
    context = super(BookListView, self).get_context_data(**kwargs)
    # context['some_data'] = 'T'
    return context'''
