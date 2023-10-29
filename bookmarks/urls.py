from django.urls import path
from . import views

appname='bookmarks'

urlpatterns = [
    path('bookmarks/', views.view_bookmarks, name='view_bookmarks'),
    path('bookmark-book/<int:book_id>/', views.bookmark_book, name='bookmark_book'),
    path('remove_bookmark/<int:book_id>/', views.remove_bookmark, name='remove_bookmark'),
    path('get-books-json/', views.get_books_json, name='get_books_json'),
]
