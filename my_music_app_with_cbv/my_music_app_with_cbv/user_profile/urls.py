from django.urls import path

from my_music_app_with_cbv.user_profile import views

urlpatterns = (
    path('details/', views.profile_details, name='profile-details'),
    path('delete/', views.profile_delete, name='profile-delete')
)