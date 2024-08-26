from django import forms
from world_of_speed.profilee.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'username',
            'email',
            'age',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }