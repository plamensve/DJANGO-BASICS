from django.urls import path, include

from my_music_app_with_cbv.album import views

urlpatterns = (
    path('add/', views.album_add, name='album-add'),
    path('<int:pk>/', include([
        path('details/', views.album_details, name='album-details'),
        path('edit/', views.album_edit, name='album-edit'),
        path('delete/', views.album_delete, name='album-delete'),
    ]))
)