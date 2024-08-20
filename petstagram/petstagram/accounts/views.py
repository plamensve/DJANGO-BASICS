from django.shortcuts import render


def register(request):
    context = {}

    return render(request, 'accounts/register-page.html')


def login(request):
    context = {}

    return render(request, 'accounts/login-page.html')


def show_profile_details(request, pk):
    context = {'pk': pk}

    return render(request, 'accounts/profile-details-page.html', context)


def edit_profile(request):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request):
    return render(request, 'accounts/profile-delete-page.html')
