from django.shortcuts import render
from django.shortcuts import render, redirect
from fruitipedia_app.fruits.forms import CategoryAddForm, AddFruitForm
from fruitipedia_app.fruits.models import Fruit
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def index(request):
    print(request)
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits
    }
    return render(request, 'common/dashboard.html', context)


class CreateFruitView(CreateView):
    model = Fruit
    form_class = AddFruitForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')


def details_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()

    context = {
        'fruit': fruit,
    }

    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, pk):
    return render(request, 'fruits/edit-fruit.html')


def delete_fruit(request, pk):
    return render(request, 'fruits/delete-fruit.html')


def create_category(request):
    if request.method == 'POST':
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CategoryAddForm()

    context = {
        'form': form
    }
    return render(request, 'categories/create-category.html', context)

#trest