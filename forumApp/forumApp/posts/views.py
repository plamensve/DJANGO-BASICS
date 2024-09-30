from django.shortcuts import render, redirect

from forumApp.posts.forms import BaseForm, PostsForm
from forumApp.posts.models import Posts


# Create your views here.
def index(request):
    added_post = PostsForm(request.POST or None)

    context = {
        'form': added_post,
    }

    if request.method == 'POST' and added_post.is_valid():
        added_post.save()
        return redirect('dashboard')

    return render(request, 'base.html', context)


def edit_post(request):
    pass


def delete_post(request):
    pass


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
