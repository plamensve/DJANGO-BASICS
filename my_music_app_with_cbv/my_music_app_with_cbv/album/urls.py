from django.urls import path

from my_music_app_with_cbv.album import views

urlpatterns = (
    path('add/', views.album_add, name='album-add'),
)