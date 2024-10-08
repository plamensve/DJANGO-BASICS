from django.urls import path

from petstagram_ws1.accounts.views import register, login, profile, delete_profile, edit_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('profile/<int:pk>/edit/', edit_profile, name='edit_profile'),
    path('profile/<int:pk>/delete/', delete_profile, name='delete_profile'),

]

