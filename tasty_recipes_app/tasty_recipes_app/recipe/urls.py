from django.urls import path

from tasty_recipes_app.recipe import views

urlpatterns = (
    path('catalogue/', views.catalogue_page, name='catalogue-page'),
    path('create/', views.create_recipe_page, name='recipe_create_page'),
    path('<int:pk>/details/', views.details_recipe_page, name='recipe_details_page'),
    path('<int:pk>/edit/', views.edit_recipe_page, name='edit_recipe_page'),
    path('<int:pk>/delete/', views.delete_recipe_page, name='delete_recipe_page'),
)