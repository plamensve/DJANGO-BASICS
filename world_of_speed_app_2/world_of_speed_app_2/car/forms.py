from django import forms

from world_of_speed_app_2.car.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']

        widgets = {
            'type': forms.Select(attrs={'placeholder': 'Type'}),
            'model': forms.TextInput(attrs={'placeholder': 'Model'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Year'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'https://...'}),
        }