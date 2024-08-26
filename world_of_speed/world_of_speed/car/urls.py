from django.urls import path

from world_of_speed.car.views import catalogue, car_create, car_details, car_edit, car_delete

urlpatterns = (
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', car_create, name='car-create'),
    path('<int:pk>/details/', car_details, name='car-details'),
    path('<int:pk>/edit', car_edit, name='car-edit'),
    path('<int:pk>/delete', car_delete, name='car-delete')
)