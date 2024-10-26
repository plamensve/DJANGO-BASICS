from django.shortcuts import render, redirect

from world_of_speed_app_2.car.models import Car
from world_of_speed_app_2.user_profile.forms import CreateProfileForm
from world_of_speed_app_2.user_profile.models import Profile


def create_profile(request):
    profile_form = CreateProfileForm(request.POST or None)

    if profile_form.is_valid():
        profile_form.save()
        return redirect('home-page')

    context = {
        'profile_form': profile_form
    }

    return render(request, 'profile/profile-create.html', context=context)


def details_profile(request):
    user_profile = Profile.objects.first()
    user_cars = Car.objects.filter(owner_id=user_profile)
    total_price = sum(car.price for car in user_cars)

    context = {
        'user_profile': user_profile,
        'total_price': total_price
    }

    return render(request, 'profile/profile-details.html', context=context)


def edit_profile(request):
    user_profile = Profile.objects.first()
    profile_form = CreateProfileForm(request.POST or None, instance=user_profile)

    if profile_form.is_valid():
        profile_form.save()
        return redirect('details-profile')

    context = {
        'profile_form': profile_form
    }

    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    user_profile = Profile.objects.first()
    if request.method == 'POST':
        user_profile.delete()
        return redirect('home-page')

    return render(request, 'profile/profile-delete.html')
