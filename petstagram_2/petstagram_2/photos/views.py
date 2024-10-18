from django.shortcuts import render, redirect

from petstagram_2.common.forms import CommentForm
from petstagram_2.pets.models import Pet
from petstagram_2.photos.forms import PhotoCreateForm, PhotoEditForm
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
    print('see details button is here')
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()  #TODO : трябва да се коригира заявката
    comments = photo.comment_set.all()[:1]
    comment_form = CommentForm()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, 'photos/photo-details-page.html', context=context)


def photo_edit_page(request, pk):
    photo = Photo.objects.get(pk=pk)

    if request.method == 'POST':
        pet_photo_edit_form = PhotoEditForm(request.POST, request.FILES, instance=photo)

        if pet_photo_edit_form.is_valid():
            pet_photo_edit_form.save()
            return redirect('photo-details-page', pk=photo.pk)
    else:
        pet_photo_edit_form = PhotoEditForm(instance=photo)

    related_pet = photo.tagged_pets.all()

    context = {
        'form_photo_edit': pet_photo_edit_form,
        'related_pet': related_pet,
        'photo': photo
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home-page')
