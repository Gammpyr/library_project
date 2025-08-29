from django.urls import path
from library import views

app_name = 'library'

urlpatterns = [
    path('books_list/', views.books_list, name='books_list'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
]
