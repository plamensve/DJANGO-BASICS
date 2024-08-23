from django.shortcuts import render

from templates_advanced.main_app.form import UserForm
from templates_advanced.main_app.models import Users


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UserForm()

    user = Users.objects.first()
    photo_1 = user.photo_1
    photo_2 = user.photo_2

    context = {
        'form': form,
        'photo_1': photo_1,
        'photo_2': photo_2

    }

    return render(request, 'index.html', context)
