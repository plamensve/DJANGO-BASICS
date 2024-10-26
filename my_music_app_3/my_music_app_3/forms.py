from django import forms

from my_music_app_3.album.models import Album


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist_name', 'genre', 'description', 'image_url', 'price')

        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist_name': forms.TextInput(attrs={'placeholder': 'Artist Name'}),
            'genre': forms.Select(attrs={'placeholder': 'Genre'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price'})
        }