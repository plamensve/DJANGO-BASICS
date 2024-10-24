from django.shortcuts import render

from tasty_recipes_app.user_profile.models import Profile


def home_page(request):
    return render(request, 'home-page.html')
