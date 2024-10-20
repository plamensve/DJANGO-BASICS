from django.urls import path

from my_music_app_2.album import views

urlpatterns = (
    path('add/', views.add_album_page, name='add_album_page'),
    path('<int:pk>/details', views.details_page, name='details_page'),
    path('<int:pk>/edit', views.edit_album_page, name='edit_album_page'),
    path('<int:pk>/delete', views.delete_album, name='delete_album_page'),
)