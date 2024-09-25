from django.urls import path

from petstagram_ws1.photos.views import add_photo, details_photo, edit_photo

urlpatterns = [
    path('add/', add_photo, name='add_photo'),
    path('<int:pk>/', details_photo, name='details_photo'),
    path('<int:pk>/edit/', edit_photo, name='edit_photo')
]