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
