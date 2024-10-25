from django.shortcuts import render


def create_profile(request):
    return render(request, 'profile/profile-create.html')


def details_profile(request):
    return render(request, 'profile/profile-details.html')


def edit_profile(request):
    return render(request, 'profile/profile-edit.html')


def delete_profile(request):
    return render(request, 'profile/profile-delete.html')
