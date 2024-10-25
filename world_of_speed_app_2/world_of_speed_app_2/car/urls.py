from django.urls import path

from world_of_speed_app_2.car import views

urlpatterns = (
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.car_create, name='car_create'),
    path('<int:pk>/details/', views.car_details, name='car_details'),
    path('<int:pk>/edit/', views.car_edit, name='car_edit'),
    path('<int:pk>/delete/', views.car_delete, name='car_delete'),
)