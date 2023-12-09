from django.urls import path
from . import views

app_name = 'collection'

urlpatterns = [
    path('my-collections/', views.my_collections, name='my_collections'),
    path('add-book/<int:book_id>', views.add_book_to_collection, name='add_book_to_collection'),
    path('remove-book/<int:collection_book_id>', views.remove_book_from_collection, name='remove_book_from_collection'),
    path('collections_flutter/', views.collections_flutter, name='collections_flutter'),
    path('add_collection_flutter/', views.add_collection_flutter, name='add_collection_flutter'),
    path('remove_collection_flutter/', views.remove_collection_flutter, name='remove_collection_flutter'),
]