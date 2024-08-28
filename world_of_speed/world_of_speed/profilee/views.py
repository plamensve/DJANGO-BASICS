from django.shortcuts import render, redirect

from world_of_speed.car.models import Car
from world_of_speed.profilee.forms import CreateProfileForm, EditProfileForm
from world_of_speed.profilee.models import Profile


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
    profile = Profile.objects.first()
    cars = Car.objects.all()
    total_price = 0

    for car in cars:
        total_price += car.price

    context = {
        'profile': profile,
        'total_price': f"{total_price:.3f}"
    }

    return render(request, 'profile-details.html', context)


def profile_edit(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile.save()
            return redirect('profile-details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    return render(request, 'profile-delete.html')
