from django import forms

from my_music_app_2.album.models import Album


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'genre', 'description', 'image_field', 'price']
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'genre': forms.Select(attrs={'placeholder': '------'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_field': forms.TextInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }