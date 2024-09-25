from django.urls import path

from petstagram_ws1.pets.views import add_pets, pet_details, pet_edit, pet_delete

urlpatterns = [
    path('add/', add_pets, name='pets'),
    path('<str:username>/pet/<slug:pet_slug>/', pet_details, name='pet_details'),
    path('<str:username>/pet/<slug:pet_slug>/edit', pet_edit, name='pet_edit'),
    path('<str:username>/pet/<slug:pet_slug>/delete', pet_delete, name='pet_delete')
]