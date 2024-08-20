from django.urls import path, include
from petstagram.common.views import home_page

urlpatterns = path('', home_page, name='home-page-common'),

