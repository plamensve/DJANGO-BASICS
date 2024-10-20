from django.urls import path

from my_music_app_2.common import views

urlpatterns = (
    path('', views.home_no_profile, name='home_no_profile'),
    path('', views.home_with_profile, name='home_with_profile')  # TODO: should set the logic when the user has profile and has not profile
)