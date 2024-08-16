import time

from django.http import HttpResponse
from django.shortcuts import render

from URLS_AND_VIEWS.main_app.models import employee


def index(request):
    user = employee.objects.all()

    result = []

    for u in user:
        result.append(f"{u.name} - {u.email}")

    context = {'result': result}
    return render(request, 'index.html', context)


def workers(request, pk):
    user = employee.objects.all()

    result = [f"{u.name} - {u.email}" for u in user if u.id == pk]

    context = {'result': result}
    return render(request, 'index.html', context)
