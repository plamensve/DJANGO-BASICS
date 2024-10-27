from django.urls import path

from django_basics_regular_exam.author import views

urlpatterns = (
    path('create/', views.create_author, name='create-author'),
    path('details/', views.details_author, name='details-author'),
    path('edit/', views.edit_author, name='edit-author'),
    path('delete/', views.delete_author, name='delete-author'),
)