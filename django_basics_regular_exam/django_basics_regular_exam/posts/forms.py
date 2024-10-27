from django import forms

from django_basics_regular_exam.posts.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image_url', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
            'content': forms.Textarea(
                attrs={'placeholder': 'Share some interesting facts about your adorable pets...'}),
        }


class ReadOnlyPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image_url', 'content')

    def __init__(self, *args, **kwargs):
        super(ReadOnlyPostForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
