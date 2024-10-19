from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

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

class PetDetailsPage(DetailView):
    model = Pet
    slug_url_kwarg = 'pet_slug'
    template_name = 'pets/pet-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.photo_set.all()
        context['comment_form'] = CommentForm()
        return context


# def pet_details_page(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     all_photos = pet.photo_set.all()
#     comment_form = CommentForm()
#
#     context = {
#         'pet': pet,
#         'all_photos': all_photos,
#         'comment_form': comment_form,
#     }
#
#     return render(request, 'pets/pet-details-page.html', context)

class PetEditPage(UpdateView):
    model = Pet
    form_class = PetForm
    slug_url_kwarg = 'pet_slug'
    template_name = 'pets/pet-edit-page.html'
    success_url = reverse_lazy('pet-details-page', kwargs={'username': '<username>',
                                                           'pet_slug': '<pet_slug>'})

    def get_success_url(self):
        return reverse_lazy('pet-details-page', kwargs={'username': self.kwargs['username'],
                                                        'pet_slug': self.kwargs['pet_slug']})


# def pet_edit_page(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     if request.method == 'GET':
#         form = PetForm(instance=pet, initial=pet.__dict__)
#     else:
#         form = PetForm(request.POST, instance=pet)
#         if form.is_valid():
#             form.save()
#             return redirect('pet-details-page', username, pet_slug)
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'pets/pet-edit-page.html', context=context)

class PetDeletePage(DeleteView):
    model = Pet
    slug_url_kwarg = 'pet_slug'
    template_name = 'pets/pet-delete-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': 1})


# def pet_delete_page(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     if request.method == 'POST':
#         pet.delete()
#         return redirect('profile-details', pk=1)
#     form = PetDeleteForm(initial=pet.__dict__)
#
#     context = {
#         'form': form
#     }
#     return render(request, 'pets/pet-delete-page.html', context=context)
