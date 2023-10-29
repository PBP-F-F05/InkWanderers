from django.urls import path
from . import views

app_name = 'collection'

urlpatterns = [
    #path('create/', views.create_collection, name='create_collection'),
    path('my-collections/', views.my_collections, name='my_collections'),
    path('add-book/<int:book_id>', views.add_book_to_collection, name='add_book_to_collection'),
    path('remove-book/<int:collection_book_id>', views.remove_book_from_collection, name='remove_book_from_collection'),
]