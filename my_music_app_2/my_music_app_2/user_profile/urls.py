from django.urls import path

from my_music_app_2.user_profile import views

urlpatterns = (
    path('details/', views.profile_details, name='profile_details'),
    path('delete/', views.profile_delete, name='profile_delete'),
)