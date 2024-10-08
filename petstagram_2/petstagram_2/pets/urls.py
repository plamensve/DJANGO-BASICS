from django.urls import path
from petstagram_2.pets import views

urlpatterns = (
    path('add/', views.pet_add_page, name='pet-add-page'),
    path('<str:username>/pet/<slug:pet_slug>/', views.pet_details_page, name='pet-details-page'),
    path('<str:username>/pet/<slug:pet_slug>/edit/', views.pet_edit_page, name='pet-edit-page'),
    path('<str:username>/pet/<slug:pet_slug>/delete/', views.pet_delete_page, name='pet-delete-page'),

)