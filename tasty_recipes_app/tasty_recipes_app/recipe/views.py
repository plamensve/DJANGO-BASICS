from django.shortcuts import render, redirect, get_object_or_404

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
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')

    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'recipe/details-recipe.html', context)


def edit_recipe_page(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = CreateRecipeFrom(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('catalogue-page')

    context = {
        'form': form,
        'recipe': recipe
    }

    return render(request, 'recipe/edit-recipe.html', context)


def delete_recipe_page(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = CreateRecipeFrom(request.POST or None, instance=recipe)

    for field in form.fields.values():
        field.widget.attrs['readonly'] = True
        field.widget.attrs['disabled'] = True

    if request.method == 'POST':
        recipe.delete()
        return redirect('catalogue-page')

    context = {
        'form': form,
        'recipe': recipe
    }

    return render(request, 'recipe/delete-recipe.html', context)
