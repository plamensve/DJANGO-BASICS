from django.urls import path

from forumApp.posts.views import books, notifications, settings, profile, edit_post, \
    delete_post, delete_page, add_post, BaseForm, DashboardView

urlpatterns = [
    # path('', Index.as_view(), name='index'),
    path('', BaseForm.as_view(), name='index'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/<int:pk>/edit/', edit_post, name='edit_post'),
    path('dashboard/<int:pk>/delete/', delete_post, name='delete_post'),
    path('dashboard/<int:pk>/delete_post', delete_page, name='delete_page'),


    path('add_post/', add_post, name='add-post'),
    path('books/', books, name='books'),
    path('notifications/', notifications, name='notifications'),
    path('settings/', settings, name='settings'),
    path('profile/', profile, name='profile')
]

