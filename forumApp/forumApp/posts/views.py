from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'base.html')


def dashboard(request):
    return render(request, 'posts/bashboard.html')


def games(request):
    return render(request, 'games.html')


def books(request):
    return render(request, 'books.html')


def notifications(request):
    return render(request, 'notifications.html')


def settings(request):
    return render(request, 'settings.html')


def profile(request):
    return render(request, 'profile.html')
