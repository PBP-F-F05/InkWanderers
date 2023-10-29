from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    
    path('', views.show_main, name='show_main'),
    path('get_books_json/', views.get_books_json, name='get_books_json'),
    path('add_book_ajax/', views.add_book_ajax, name='add_book_ajax'),
    path('remove_book_ajax/<int:id>', views.remove_book_ajax , name='remove_book_ajax'),
]