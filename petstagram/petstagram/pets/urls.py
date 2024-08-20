from django.urls import path

from petstagram.pets.views import add_pets, pet_details, pet_delete, pet_edit

urlpatterns = (path('add/', add_pets, name='add-pets'),
               path('<str:username>/pet/<slug:pet_slug>/', pet_details, name='details-pet'),
               path('<str:username>/pet/<slug:pet_slug>/edit/', pet_delete, name='edit-pet'),
               path('<str:username>/pet/<slug:pet_slug>/delete/', pet_edit, name='delete-pet'))
