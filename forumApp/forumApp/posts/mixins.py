from django import forms


class DisableFieldsMixin(forms.Form):
    disabled_fields = ('__all__', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name in self.disabled_fields or self.disabled_fields[0] == '__all__':
                field.disabled = True
