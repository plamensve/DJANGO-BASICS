from django.urls import path

from forumApp.posts.views import index, dashboard, games, books, notifications, settings, profile

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('games/', games, name='games'),
    path('books/', books, name='books'),
    path('notifications/', notifications, name='notifications'),
    path('settings/', settings, name='settings'),
    path('profile/', profile, name='profile')
]