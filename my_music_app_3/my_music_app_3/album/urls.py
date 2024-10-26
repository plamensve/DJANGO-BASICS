from django.urls import path, include

from my_music_app_3.album import views

urlpatterns = (
    path('add/', views.add_album, name='add_album'),
    path('<int:pk>/', include([
        path('details/', views.details_album, name='details_album'),
        path('edit/', views.edit_album, name='edit_album'),
        path('delete/', views.delete_album, name='delete_album'),
    ]))
)