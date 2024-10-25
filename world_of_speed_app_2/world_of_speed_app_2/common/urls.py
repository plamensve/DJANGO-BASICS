from django.urls import path

from world_of_speed_app_2.common import views

urlpatterns = (
    path('', views.home_page, name='home-page'),
)