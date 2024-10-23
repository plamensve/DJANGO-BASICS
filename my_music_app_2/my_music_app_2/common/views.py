from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from my_music_app_2.album.models import Album
from my_music_app_2.common.forms import CreateProfileForm
from my_music_app_2.utils import get_user_obj


class HomePageView(FormMixin, ListView):
    model = Album
    form_class = CreateProfileForm
    success_url = reverse_lazy('home-page')

    template_name_with_profile = 'home-with-profile.html'
    template_name_no_profile = 'home-no-profile.html'

    def get_template_names(self):
        profile = get_user_obj(self.request)

        if profile:
            return [self.template_name_with_profile]

        return [self.template_name_no_profile]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        context['form'] = self.get_form()
        context['profile'] = get_user_obj(self.request)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(self.success_url)
        else:
            self.object_list = self.get_queryset()
            return self.form_invalid(form)

