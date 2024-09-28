from django import forms
from django.core.validators import MinValueValidator


class BaseForm(forms.Form):
    first_name = forms.CharField(
        max_length=10
    )

    second_name = forms.CharField(
        max_length=10
    )

    age = forms.IntegerField(
        validators=[
            MinValueValidator(18)
        ]
    )
