from django.shortcuts import render

from petstagram_ws1.accounts.models import UserProfile
from django.shortcuts import get_object_or_404


def register(request):
    return render(request, 'accounts/register-page.html')


def login(request):
    return render(request, 'accounts/login-page.html')


def profile(request, pk):

    return render(request, 'accounts/profile-details-page.html', context)


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
