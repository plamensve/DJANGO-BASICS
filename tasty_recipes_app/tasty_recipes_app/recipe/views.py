from django.shortcuts import render, redirect

from tasty_recipes_app.recipe.forms import CreateRecipeFrom
from tasty_recipes_app.recipe.models import Recipe
from tasty_recipes_app.user_profile.models import Profile


def catalogue_page(request):
    catalogue = Recipe.objects.all()

    context = {
        'catalogue': catalogue,
    }

    return render(request, 'recipe/catalogue.html', context)


def create_recipe_page(request):
    form = CreateRecipeFrom(request.POST or None)

    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.author = Profile.objects.first()
        recipe.save()
        return redirect('catalogue-page')

    context = {
        'form': form,
    }

    return render(request, 'recipe/create-recipe.html', context)


def details_recipe_page(request, pk):
    return render(request, 'recipe/details-recipe.html')


def edit_recipe_page(request, pk):
    return render(request, 'recipe/edit-recipe.html')


def delete_recipe_page(request, pk):
    return render(request, 'recipe/delete-recipe.html')
