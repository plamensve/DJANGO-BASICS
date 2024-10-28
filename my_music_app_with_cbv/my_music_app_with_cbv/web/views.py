from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from .forms import CreateProfileForm
from ..album.models import Album
from ..utls import get_user_object


class HomePageView(FormMixin, ListView):
    model = Album
    form_class = CreateProfileForm
    success_url = reverse_lazy('home-page')

    def get_template_names(self):
        profile = get_user_object()  # None or QuerySet

        if profile:
            return ['profile/home-with-profile.html']
        return ['profile/home-no-profile.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    #test