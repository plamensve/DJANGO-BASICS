from django.shortcuts import render, redirect

from tasty_recipes_app.user_profile.forms import CreateProfileForm


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
    return render(request, 'profile/details-profile.html')


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')
