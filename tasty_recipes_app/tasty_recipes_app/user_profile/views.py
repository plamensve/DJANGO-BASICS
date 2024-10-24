from django.shortcuts import render, redirect, get_object_or_404

from tasty_recipes_app.recipe.models import Recipe
from tasty_recipes_app.user_profile.forms import CreateProfileForm
from tasty_recipes_app.user_profile.models import Profile


def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('catalogue-page')

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.first()
    profile_chef = profile.chef
    recipe_count = Recipe.objects.filter(author_id=profile.id).count()

    context = {
        'profile': profile,
        'profile_chef': profile_chef,
        'recipe_count': recipe_count,
    }

    return render(request, 'profile/details-profile.html', context=context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')
    else:
        form = CreateProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        profile.delete()
        return redirect('home-page')

    context = {
        'profile': profile
    }

    return render(request, 'profile/delete-profile.html', context)
