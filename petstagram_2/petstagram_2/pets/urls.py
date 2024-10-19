from django.urls import path
from petstagram_2.pets import views

urlpatterns = (
    path('add/', views.PetAddPage.as_view(), name='pet-add-page'),
    path('<str:username>/pet/<slug:pet_slug>/', views.PetDetailsPage.as_view(), name='pet-details-page'),
    path('<str:username>/pet/<slug:pet_slug>/edit/', views.PetEditPage.as_view(), name='pet-edit-page'),
    path('<str:username>/pet/<slug:pet_slug>/delete/', views.PetDeletePage.as_view(), name='pet-delete-page'),

)