from django.shortcuts import render


def catalogue(request):
    return render(request, 'car/catalogue.html')


def car_create(request):
    return render(request, 'car/car-create.html')


def car_details(request, pk):
    return render(request, 'car/car-details.html')


def car_edit(request, pk):
    return render(request, 'car/car-edit.html')


def car_delete(request, pk):
    return render(request, 'car/car-delete.html')
