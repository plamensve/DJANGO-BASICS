from django import forms

from web.models import TruckRoots


class IndexForm(forms.ModelForm):
    class Meta:
        model = TruckRoots
        fields = '__all__'
