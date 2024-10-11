from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Posts


class BaseForm(forms.Form):
    first_name = forms.CharField(
        max_length=10,
    )

    second_name = forms.CharField(
        max_length=10
    )

    age = forms.IntegerField(
        validators=[
            MinValueValidator(18)
        ]
    )

    text_area = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 80, 'rows': 15})
    )


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'

        labels = {
            'image': ''
        }

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if author[0] != author[0].upper():
            raise ValidationError('Author should start with capital letter!')

        return author

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('author')
        content = cleaned_data.get('content')

        if name and content and name in content:
            raise ValidationError('The author name cannot be included in content!')

        return cleaned_data

class PostDeleteForm(PostsForm, DisableFieldsMixin):
    pass

