from django.urls import path

from tasty_recipes_app.user_profile import views

urlpatterns = (
    path('create/', views.create_profile, name='create-profile'),
    path('details/', views.details_profile, name='details-profile'),
    path('edit/', views.edit_profile, name='edit-profile'),
    path('delete/', views.delete_profile, name='delete-profile'),
)