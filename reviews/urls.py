from django.urls import path
from reviews.views import show_review, add_review, show_my_reviews, show_json, show_json_by_id, delete_review_ajax, get_review_json


app_name = 'reviews'

urlpatterns = [
    path('<int:id>', show_review, name='show_review'),
    path('add-review/<int:id>',add_review,name="add_review"),
    path('my-reviews/', show_my_reviews, name="my_reviews"),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('delete-review-ajax/', delete_review_ajax, name='remove_review_ajax'),
    path('get-review/', get_review_json, name='get_review_json')
]