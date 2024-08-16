from django.urls import path

from URLS_AND_VIEWS.main_app import views

urlpatterns = [
    path('', views.index),
    path('employee/<int:pk>', views.workers)
]