from django.urls import path
from reviews.views import show_review, add_review, show_my_reviews, show_json, show_json_by_id, edit_review_ajax, get_review_json,\
      add_review_flutter, show_json_flutter, show_review_by_book, get_book_json_id,edit_review_flutter



app_name = 'reviews'

urlpatterns = [
    path('<int:id>', show_review, name='show_review'),
    path('add-review/<int:id>',add_review,name="add_review"),
    path('my-reviews/', show_my_reviews, name="my_reviews"),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('my-reviews/edit_review_ajax/<int:id>/', edit_review_ajax, name='edit_review_ajax'),
    path('get-review/', get_review_json, name='get_review_json'),
    path('add-review-flutter/<int:id>', add_review_flutter, name='add_review_flutter'),
    path('try/', show_json_flutter, name='tes'),
    path('show-reviews/<int:id>', show_review_by_book, name='show_review_by_book'),
    path('get-book/<int:id>', get_book_json_id, name='get-book-json-id'),
    path('edit-review-flutter/<int:id>', edit_review_flutter, name='edit_review_flutter')
]