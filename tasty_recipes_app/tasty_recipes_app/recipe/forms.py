from django import forms

from tasty_recipes_app.recipe.models import Recipe


class CreateRecipeFrom(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author', )

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',  # Добави класове за стилизиране, ако е нужно
                'placeholder': 'Recipe Title',
            }),
            'cuisine_type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Cuisine Type',
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'ingredient1, ingredient2, ...',  # Плейсхолдер за съставките
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter detailed instructions here...',  # Плейсхолдер за инструкции
            }),
            'cooking_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cooking time in minutes',
            }),
            'image_url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional image URL here...',  # Плейсхолдер за URL на изображение
            }),
        }

        help_texts = {
            'ingredients': 'Ingredients must be separated by a comma and space.',  # Текст за помощ за съставките
            'cooking_time': 'Provide the cooking time in minutes.',  # Текст за помощ за времето за готвене
        }