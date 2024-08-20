from django.urls import path

from petstagram.photos.views import add_photo, details_page, edit_photo

urlpatterns = (path('add/', add_photo, name='add-photo'),
               path('<int:pk>', details_page, name='details-page'),
               path('<int:pk>/edit/', edit_photo, name='edit-photo'),)