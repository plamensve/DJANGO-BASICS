from django.shortcuts import render, redirect

from world_of_speed.car.forms import CreateCarForm
from world_of_speed.car.models import Car, Profile


def catalogue(request):
    cars = Car.objects.all()

    context = {
        'cars': cars,
        'count_of_car': len(cars)
    }

    return render(request, 'catalogue.html', context)


def car_create(request):
    form = CreateCarForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            car = form.save(commit=False)
            owner = Profile.objects.first()

            if owner:
                car.owner_id = owner.id
                car.save()

            return redirect('catalogue')

    context = {
        'form': form
    }
    return render(request, 'car-create.html', context)


def car_details(request, pk):
    car = Car.objects.get(pk=pk)

    context = {
        'car': car
    }

    return render(request, 'car-details.html', context)


def car_edit(request, pk):
    return render(request, 'car-edit.html')


def car_delete(request, pk):
    return render(request, 'car-delete.html')
