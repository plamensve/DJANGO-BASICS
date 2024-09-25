from django.contrib import admin

from petstagram_ws1.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet_slug')


