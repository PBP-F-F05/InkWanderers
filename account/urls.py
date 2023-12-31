from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'), 

    path('profile/', views.profile, name='profile'), 
    # path('edit_profile/', views.edit_profile, name='edit_profile'), 

    path('logout/', views.logout_user, name='logout_user'),
    path('password_change/', views.password_change, name='password_change'),
    path('password_change_by_ajax/', views.password_change_by_ajax, name='password_change_by_ajax'),

    path('view_books/', views.view_books, name='view_books'),
    path('view_rank_books/', views.view_rank_book, name='view_rank_book'),
    path('view_history_books/', views.view_history_book, name='view_history_book'),

    path('add_book/<int:id>/', views.add_book, name='add_book'),
    path('get-rank-book-json/', views.show_json_by_highest_number, name='get_rank_book_json'),
    path('get-history-book-json/', views.show_json_history_book, name='get_history_book_json'),

    # Flutter related
    path('get-profile-json/', views.show_json_profile, name='get_profile_json'),
    path('get-user-json/', views.show_json_user, name='show_json_user'),
    path('logout_flutter/', views.logout_user_flutter, name='logout_user_flutter'),
    path('change_password_flutter/', views.change_password_flutter, name='logout_user_flutter'),
    path('get-history-book-json-flutter/', views.show_json_history_book_flutter, name='get_history_book_json_flutter'),
    path('get-rank-book-json-flutter/', views.show_json_rank_book_flutter, name='get_history_book_json_flutter'),

    path('book_json_flutter/', views.view_book_json_flutter, name='view_book_json_flutter'),





]
