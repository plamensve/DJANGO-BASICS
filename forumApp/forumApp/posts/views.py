from django.shortcuts import render, redirect

from forumApp.posts.forms import BaseForm, StudentForm
from forumApp.posts.models import Posts, PersonInfor, StudentWithChoices


# Create your views here.
def index(request):
    form = BaseForm(request.POST or None)
    s_form = StudentForm(request.POST or None)  # Използвай StudentForm вместо модела StudentWithChoices

    context = {
        'form': form,
        's_form': s_form
    }

    if request.method == 'POST' and s_form.is_valid():
        s_form.save()

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
