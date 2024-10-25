from django.shortcuts import render, redirect

from world_of_speed_app_2.car.forms import CarCreateForm
from world_of_speed_app_2.car.models import Car
from world_of_speed_app_2.user_profile.models import Profile


def catalogue(request):
    all_cars = Car.objects.all()
    all_cars_count = all_cars.count()

    context = {
        'all_cars': all_cars,
        'all_cars_count': all_cars_count,
    }

    return render(request, 'car/catalogue.html', context=context)


def car_create(request):
    car_create_form = CarCreateForm(request.POST or None)

    if car_create_form.is_valid():
        car = car_create_form.save(commit=False)
        car.owner = Profile.objects.first()
        car.save()  # Save car instance to the database.
        return redirect('catalogue')  # Redirect to car catalogue page after form submission.

    context = {
        'car_create_form': car_create_form
    }

    return render(request, 'car/car-create.html', context=context)


def car_details(request, pk):
    car = Car.objects.get(pk=pk)

    context = {
        'car': car
    }

    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.get(pk=pk)
    car_edit_form = CarCreateForm(request.POST or None, instance=car)

    if car_edit_form.is_valid():
        car_edit_form.save()
        return redirect('catalogue')

    context = {
        'car': car,
        'car_edit_form': car_edit_form,

    }

    return render(request, 'car/car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.get(pk=pk)
    car_delete_form = CarCreateForm(request.POST or None, instance=car)

    for field in car_delete_form.fields.values():
        field.widget.attrs['readonly'] = True
        field.widget.attrs['disabled'] = True

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    context = {
        'car': car,
        'car_delete_form': car_delete_form,
    }

    return render(request, 'car/car-delete.html', context)
