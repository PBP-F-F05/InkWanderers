from django.urls import path
from . import views

appname='bookmarks'

urlpatterns = [
    path('bookmarks/', views.view_bookmarks, name='view_bookmarks'),
    path('bookmark-book/<int:book_id>/', views.bookmark_book, name='bookmark_book'),
    path('remove_bookmark/<int:book_id>/', views.remove_bookmark, name='remove_bookmark'),
    path('get-books-json/', views.get_books_json, name='get_books_json'),
    path('get_bookmarks/', views.get_bookmarks, name='get_bookmarks'),
    path('bookmark_book_flutter/', views.bookmark_book_flutter, name='bookmark_book_flutter'),
    path('remove_bookmark_flutter/', views.remove_bookmark_flutter, name='remove_bookmark_flutter'),
]
