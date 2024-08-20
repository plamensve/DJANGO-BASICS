from django.shortcuts import render


def add_pets(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details(request, username, pet_slug):
    return render(request, 'pets/pet-details-page.html')


def pet_delete(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')


def pet_edit(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')
