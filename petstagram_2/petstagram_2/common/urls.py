from django.urls import path

from petstagram_2.common import views

urlpatterns = (
    path('', views.home_page, name='home-page'),
    path('like/<int:photo_id>/', views.like_functionality, name='like'),
)