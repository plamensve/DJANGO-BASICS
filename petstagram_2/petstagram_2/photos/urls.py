from django.urls import path

from petstagram_2.photos import views

urlpatterns = (
    path('add/', views.photo_add_page, name='photo-add-page'),
    path('<int:pk>/', views.photo_details_page, name='photo-details-page'),
    path('<int:pk>/edit/', views.photo_edit_page, name='photo-edit-page'),
    path('delete/<int:pk>/', views.delete_photo, name='delete-photo')
)