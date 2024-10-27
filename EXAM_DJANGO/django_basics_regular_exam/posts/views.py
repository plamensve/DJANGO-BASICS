from django.shortcuts import render, redirect, get_object_or_404

from django_basics_regular_exam.author.models import Author
from django_basics_regular_exam.posts.forms import CreatePostForm, ReadOnlyPostForm
from django_basics_regular_exam.posts.models import Post


def create_post(request):
    form = CreatePostForm(request.POST or None)

    if form.is_valid():
        post = form.save(commit=False)
        author = Author.objects.first()
        post.author = author
        post.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'post/create-post.html', context)


def details_post(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'post/details-post.html', context)


def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    form = CreatePostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'post/edit-post.html', context)


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')

    form = ReadOnlyPostForm(instance=post)

    context = {
        post: post,
        'form': form,
    }

    return render(request, 'post/delete-post.html', context)
