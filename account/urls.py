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

    path('view_books/', views.view_books, name='view_books'),
    path('view_history_books/', views.view_history_book, name='view_history_book'),

    path('add_book/<int:id>/', views.add_book, name='add_book'),

]
