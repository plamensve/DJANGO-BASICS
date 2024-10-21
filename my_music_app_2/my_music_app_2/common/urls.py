from django.urls import path

from my_music_app_2.common import views
from my_music_app_2.common.views import HomePageView

urlpatterns = (
    path('', HomePageView.as_view(), name='home-page'),
)