from django.urls import path

from my_music_app.album.views import add_album, details_album, edit_album, delete_album

urlpatterns = (
    path('add/', add_album, name='add-album'),
    path('<int:pk>/details/', details_album, name='details-album'),
    path('<int:pk>/edit/', edit_album, name='edit-album'),
    path('<int:pk>/delete/', delete_album, name='delete-album'),
)