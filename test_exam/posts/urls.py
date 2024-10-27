from django.urls import path

from django_basics_regular_exam.posts import views

urlpatterns = (
    path('create/', views.create_post, name='create-post'),
    path('<int:pk>/details/', views.details_post, name='details-post'),
    path('<int:pk>/edit/', views.edit_post, name='edit-post'),
    path('<int:pk>/delete/', views.delete_post, name='delete-post')
)