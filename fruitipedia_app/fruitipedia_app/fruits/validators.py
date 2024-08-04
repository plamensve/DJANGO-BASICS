from django.core.exceptions import ValidationError


# def check_name_letters(value):
#     if not value.isalpha():
#         raise ValidationError("Fruit name should contain only letters!")

class OnlyLettersValidator:
    def __init__(self, message="Fruit name should contain only letters!"):
        self.message = message

    def __call__(self, value: str):
        if not value.isalpha():
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'fruitipedia_app.fruits.validators.OnlyLettersValidator',
            (),
            {'message': self.message}
        )
