from django import forms

from petstagram_2.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...'
                }
            ),
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        label='Search by pet name',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by pet name...',
        }),

    )

