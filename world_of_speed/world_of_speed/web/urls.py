from django.urls import path

from world_of_speed.web.views import index

urlpatterns = (
    path('', index, name='index'),
)