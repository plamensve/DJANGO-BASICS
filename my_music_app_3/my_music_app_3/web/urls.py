from django.urls import path

from my_music_app_3.web import views

urlpatterns = (
    path('', views.index, name='index'),
)