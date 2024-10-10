from django.shortcuts import render, redirect

from petstagram_2.photos.forms import PhotoCreateForm
from petstagram_2.photos.models import Photo


def photo_add_page(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home-page')

    context = {
        'form': form
    }
    return render(request, 'photos/photo-add-page.html', context)


def photo_details_page(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_to_photo.all()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }
    return render(request, 'photos/photo-details-page.html', context=context)


def photo_edit_page(request, pk):
    return render(request, 'photos/photo-edit-page.html')


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home-page')