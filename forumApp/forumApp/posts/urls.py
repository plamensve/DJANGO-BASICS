from django.urls import path

from forumApp.posts.views import index, dashboard, games, books, notifications, settings, profile, edit_post, \
    delete_post

urlpatterns = [
    path('', index, name='index'),

    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/<int:pk>/edit/', edit_post, name='edit_post'),
    path('dashboard/<int:pk>/delete/', delete_post, name='delete_post'),




    path('games/', games, name='games'),
    path('books/', books, name='books'),
    path('notifications/', notifications, name='notifications'),
    path('settings/', settings, name='settings'),
    path('profile/', profile, name='profile')
]