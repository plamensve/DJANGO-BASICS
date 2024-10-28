from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from my_music_app_with_cbv.album.models import Album
from my_music_app_with_cbv.user_profile.models import Profile
from my_music_app_with_cbv.web.forms import CreateProfileForm


class HomePageView(ListView, BaseFormView):
    model = Album
    form_class = CreateProfileForm
    success_url = reverse_lazy('home-page')

    def get_template_names(self):
        profile = Profile.objects.first()

        if profile:
            return ['profile/home-with-profile.html']
        else:
            return ['profile/home-no-profile.html']