from django.urls import path

from fruitipedia_app.fruits import views

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-fruit/', views.create_fruit, name='create-fruit'),
    path('<int:pk>/details-fruit/', views.details_fruit, name='details-fruit'),
    path('<int:pk>/edit-fruit/', views.edit_fruit, name='edit-fruit'),
    path('<int:pk>/delete-fruit/', views.delete_fruit, name='delete-fruit'),
    path('create-category/', views.create_category, name='create-category')
)