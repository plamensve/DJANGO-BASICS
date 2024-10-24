from django.shortcuts import render


def catalogue_page(request):
    return render(request, 'recipe/catalogue.html')


def create_recipe_page(request):
    return render(request, 'recipe/create-recipe.html')


def details_recipe_page(request, pk):
    return render(request, 'recipe/details-recipe.html')


def edit_recipe_page(request, pk):
    return render(request, 'recipe/edit-recipe.html')


def delete_recipe_page(request, pk):
    return render(request, 'recipe/delete-recipe.html')
