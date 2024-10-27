from django.urls import path

from django_basics_regular_exam.web import views

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
)