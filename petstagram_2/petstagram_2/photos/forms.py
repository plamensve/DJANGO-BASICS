from django import forms

from petstagram_2.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['description', 'location', 'tagged_pets']
