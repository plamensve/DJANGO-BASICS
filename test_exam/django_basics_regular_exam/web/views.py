from django.shortcuts import render

from django_basics_regular_exam.posts.models import Post


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    all_posts = Post.objects.all()

    context = {
        'all_posts': all_posts,
    }

    return render(request, 'dashboard.html', context=context)