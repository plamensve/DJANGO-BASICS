from django import forms
from django.core.validators import MinValueValidator

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



class Comments(forms.ModelForm):
    pass



















