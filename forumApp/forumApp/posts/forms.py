from django import forms
from django.core.validators import MinValueValidator

from forumApp.posts.models import StudentWithChoices


class BaseForm(forms.Form):
    STATUS_CHOICES = (
        (1, 'DRAFT'),
        (2, 'PUBLISHED'),
        (3, 'ARCHIVED')
    )

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

    is_lecturer = forms.BooleanField(

    )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
    )


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentWithChoices
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.label = f'First Name'
            field.widget.attrs['placeholder'] = f'Enter {field_name}'

            if field_name == 'status':
                field.widget = forms.RadioSelect(choices=field.choices)























