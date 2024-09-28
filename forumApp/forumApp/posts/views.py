from django.shortcuts import render, redirect

from forumApp.posts.forms import BaseForm
from forumApp.posts.models import Posts, PersonInfor


# Create your views here.
def index(request):
    form = BaseForm(request.POST or None)

    context = {
        'form': form
    }

    if request.method == 'POST' and form.is_valid():
        first_name = form.cleaned_data['first_name']
        second_name = form.cleaned_data['second_name']
        age = form.cleaned_data['age']

        person = PersonInfor(first_name=first_name, second_name=second_name, age=age)
        person.save()

    return render(request, 'base.html', context)


def dashboard(request):
    posts = Posts.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'posts/dashboard.html', context)


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


