from django.shortcuts import render, redirect

from world_of_speed.profilee.forms import CreateProfileForm


def profile_create(request):
    form = CreateProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            profile = form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'profile-create.html', context)


def profile_details(request):
    return render(request, 'profile-details.html')


def profile_edit(request):
    return render(request, 'profile-edit.html')


def profile_delete(request):
    return render(request, 'profile-delete.html')
