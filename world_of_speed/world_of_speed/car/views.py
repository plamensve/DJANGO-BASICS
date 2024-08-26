from django.shortcuts import render


def catalogue(request):
    return render(request, 'catalogue.html')


def car_create(request):
    return render(request, 'car-create.html')


def car_details(request, pk):
    return render(request, 'car-details.html')


def car_edit(request, pk):
    return render(request, 'car-edit.html')


def car_delete(request, pk):
    return render(request, 'car-delete.html')
