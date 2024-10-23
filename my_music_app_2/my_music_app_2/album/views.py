from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from my_music_app_2.album.forms import CreateAlbumForm
from my_music_app_2.album.models import Album
from my_music_app_2.utils import get_user_obj


class AlbumCreateView(CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'album/album-add.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        album = form.save(commit=False)
        form.instance.owner = get_user_obj(self.request)  # Свързване на албума с профила на потребителя
        album.save()
        return super().form_valid(form)

# def add_album_page(request):
#     form = CreateAlbumForm(request.POST or None)
#
#     if form.is_valid():
#         album = form.save(commit=False)
#         album.owner = get_user_obj(request)
#         album.save()
#         return redirect('home-page')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'album/album-add.html', context)



def details_page(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context=context)


def edit_album_page(request, pk):
    return render(request, 'album/album-edit.html')


def delete_album(request, pk):
    return render(request, 'album/album-delete.html')
