from django.shortcuts import render
from django.views.generic import ListView

from my_music_app_2.album.models import Album
from my_music_app_2.mixins import GetProfileObject
from my_music_app_2.user_profile.models import Profile


class HomePageView(ListView, GetProfileObject):
    model = Profile
    template_name_with_profile = 'home-with-profile.html'
    template_name_no_profile = 'home-no-profile.html'

    def get_template_names(self):
        profile = self.get_profile_object()

        if profile:
            return [self.template_name_with_profile]

        return [self.template_name_no_profile]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        return context
