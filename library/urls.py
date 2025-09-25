from django.urls import path
from library import views

app_name = 'library'

urlpatterns = [
    # path('books_list/', views.books_list, name='books_list'),
    # path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),

    path('', views.IndexListView.as_view(), name='home_page'),

    path('books/list/', views.BookListView.as_view(), name='book_list'),
    path('books/create/', views.BookCreateView.as_view(), name='book_create'),
    path('books/detail/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),


    path('authors/list/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('authors/detail/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('authors/update/<int:pk>/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('authors/delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='author_delete'),


]
