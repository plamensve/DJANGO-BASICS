from django.shortcuts import render

from petstagram_2.common.models import Like
from petstagram_2.pets.models import Pet
from petstagram_2.photos.models import Photo


def register(request):
    return render(request, 'accounts/register-page.html')


def login(request):
    return render(request, 'accounts/login-page.html')


def show_profile_details(request, pk):
    all_pets = Pet.objects.all()
    photo_count = Photo.objects.all()
    all_photos = Photo.objects.all()
    likes = Like.objects.all()

    context = {
        'all_pets': all_pets.count(),
        'all_photos': all_photos,
        'likes': likes.count(),
        'photo_count': photo_count.count()
    }

    return render(request, 'accounts/profile-details-page.html', context)


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
