from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from petstagram_2.common.forms import CommentForm
from petstagram_2.pets.forms import PetForm, PetDeleteForm
from petstagram_2.pets.models import Pet


# CBV - ADD pet ------------------------------------------------------------>
class PetAddPage(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})


# FBV - ADD pet ------------------------------------------------------------>

# def pet_add_page(request):
#     form = PetForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('profile-details', pk=1)
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'pets/pet-add-page.html', context)


def pet_details_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
    }

    return render(request, 'pets/pet-details-page.html', context)


def pet_edit_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details-page', username, pet_slug)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-edit-page.html', context=context)


def pet_delete_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)

    context = {
        'form': form
    }
    return render(request, 'pets/pet-delete-page.html', context=context)
