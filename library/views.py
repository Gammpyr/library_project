from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from library.forms import BookForm, AuthorForm
from library.models import Book, Author


class IndexListView(ListView):
    pass

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_date__year__gt=1800)


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_books_count'] = Book.objects.filter(author=self.object.author).count()
        return context


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:book_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:book_list')

    def get_success_url(self):
        return reverse('library:book_detail', kwargs={'pk': self.object.pk})


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('library:book_list')

class AuthorListView(ListView):
    model = Author
    template_name = 'library/author_list.html'
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/author_detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_books'] = self.object.books.all()
        context['author_books_count'] = self.object.books.count()

        return context

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    success_url = reverse_lazy('library:author_list')

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    success_url = reverse_lazy('library:author_list')
    def get_success_url(self):
        return reverse('library:author_detail', kwargs={'pk': self.object.pk})

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'library/author_confirm_delete.html'
    success_url = reverse_lazy('library:author_list')