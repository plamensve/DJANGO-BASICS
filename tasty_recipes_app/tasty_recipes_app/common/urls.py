from django.urls import path

from tasty_recipes_app.common import views

urlpatterns = (
    path('', views.home_page, name='home-page'),
)