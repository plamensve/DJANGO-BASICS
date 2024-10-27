from django.shortcuts import render, redirect

from django_basics_regular_exam.author.forms import CreateAuthorForm, EditAuthorForm
from django_basics_regular_exam.author.models import Author


def create_author(request):
    form = CreateAuthorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'author/create-author.html', context=context)


def details_author(request):
    author = Author.objects.first()
    posts_count = author.post_set.all().count()
    posts = author.post_set.all()
    last_updated_post = posts.order_by('-updated_at').first() if posts_count > 0 else None

    context = {
        'author': author,
        'posts_count': posts_count,
        'last_updated_post': last_updated_post
    }

    return render(request, 'author/details-author.html', context=context)


def edit_author(request):
    author = Author.objects.first()
    form = EditAuthorForm(request.POST or None, instance=author)

    if form.is_valid():
        form.save()
        return redirect('details-author')

    context = {
        'author': author,
        'form': form
    }

    return render(request, 'author/edit-author.html', context=context)


def delete_author(request):
    author = Author.objects.first()

    if request.method == 'POST':
        author.delete()
        return redirect('index')

    return render(request, 'author/delete-author.html')
