from django.shortcuts import render


def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def details_page(request, pk):
    return render(request, 'pets/pet-details-page.html')


def edit_photo(request, pk):
    return render(request, 'pets/pet-edit-page.html')
