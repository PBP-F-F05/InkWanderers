from django.urls import path
import book.views as views

app_name = 'book'

urlpatterns = [
    path("", views.get_books, name='get_books'),
]
