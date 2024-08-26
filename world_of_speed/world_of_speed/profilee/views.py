from django.shortcuts import render


def profile_create(request):
    return render(request, 'profile-create.html')


def profile_details(request):
    return render(request, 'profile-details.html')


def profile_edit(request):
    return render(request, 'profile-edit.html')


def profile_delete(request):
    return render(request, 'profile-delete.html')
