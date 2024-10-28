from django.urls import path

from my_music_app_with_cbv.web.views import HomePageView

urlpatterns = (
    path('', HomePageView.as_view(), name='home-page'),
)