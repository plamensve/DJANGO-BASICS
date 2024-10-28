from django.urls import path

from my_music_app_with_cbv.web import views

urlpatterns = (
    path('', views.home_page, name='home-page'),
)