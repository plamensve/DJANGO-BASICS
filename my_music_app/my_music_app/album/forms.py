from django import forms

from my_music_app.album.models import Album


class CreateAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'genre', 'description', 'image_url', 'price']

    widgets = {
        'album_name': forms.TextInput(attrs={
            'placeholder': 'Album Namee'
        }),
        'artist': forms.TextInput(attrs={
            'placeholder': 'Artist'
        }),

        'description': forms.Textarea(attrs={
            'placeholder': 'Description',
        }),
        'image_url': forms.URLInput(attrs={
            'placeholder': 'Image URL'
        }),
        'price': forms.NumberInput(attrs={
            'placeholder': 'Price'
        }),
    }
