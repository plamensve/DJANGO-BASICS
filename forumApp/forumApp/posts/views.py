from datetime import datetime

from django.contrib.auth.models import User
from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from forumApp.posts.forms import PostsForm, PostDeleteForm
from forumApp.posts.models import Posts


class Index(TemplateView):
    template_name = 'base.html'

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['base.html']
        else:
            return ['posts/add-post-page.html']


# class Index(View):
#     def get(self, request, *args, **kwargs):
#         post_form = modelform_factory(
#             Posts,
#             fields=('topic', 'author', 'content', 'image'),
#             labels={
#                 'image': ''
#             }
#         )
#
#         user_name = User.objects.get(username='admin')
#
#         context = {
#             'user_name': user_name,
#             'my_form': post_form(),
#             'last_refresh': datetime.now().strftime('%d-%m-%Y <:> %H:%M:%S')
#         }
#         return render(request, 'base.html', context)
#
#     def post(self, request, *args, **kwargs):
#         post_form = modelform_factory(
#             Posts,
#             fields=('topic', 'author', 'content', 'image')
#         )
#
#         form = post_form(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Form submitted successfully")
#         else:
#             context = {
#                 'my_form': form,
#                 'last_refresh': datetime.now().strftime('%d-%m-%Y <:> %H:%M:%S')
#             }
#             return render(request, 'base.html', context)


# def index(request):
#     last_refresh = datetime.now().strftime('%d-%m-%Y <:> %H:%M:%S')
#
#     full_form = PostsForm(request.POST or None)
#     part_form = modelform_factory(
#         Posts,
#         fields=('topic', 'author',),
#     )
#     mff = part_form(request.POST or None)
#
#     if request.method == 'POST':
#         if mff.is_valid():
#             mff.save()
#             return redirect('dashboard ')
#
#     context = {
#         'last_refresh': last_refresh,
#         'full_form': full_form,
#         'mff': mff,
#     }
#
#     return render(request, 'base.html', context)


def edit_post(request, pk):
    post = get_object_or_404(Posts, id=pk)

    if request.method == 'POST':
        edit_form = PostsForm(request.POST, instance=post)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('dashboard')
    else:
        edit_form = PostsForm(instance=post)

    context = {
        'edit_form': edit_form
    }
    return render(request, 'posts/edit-post.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Posts, id=pk)

    post.delete()
    return redirect('dashboard')


def delete_page(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    del_form = PostDeleteForm(instance=post)

    context = {
        'post': post,
        'del_form': del_form
    }
    return render(request, 'posts/delete-page.html', context)


def dashboard(request):
    posts = Posts.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    added_post = PostsForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if added_post.is_valid():
            added_post.save()
            return redirect('dashboard')

    context = {
        'post_form': added_post,
    }

    return render(request, 'posts/add-post-page.html', context)


def books(request):
    return render(request, 'books.html')


def notifications(request):
    return render(request, 'notifications.html')


def settings(request):
    return render(request, 'settings.html')


def profile(request):
    return render(request, 'profile.html')
