from django.shortcuts import render
from django.views.generic import CreateView

from world_of_speed.profilee.models import Profile
from world_of_speed.web.models import TestModel


def index(request):
    profile = Profile.objects.first()

    return render(request, 'index.html')


def profile_context_processor(request):

    profile = Profile.objects.first()

    return {'profile': profile}

class TestModelCreateView(CreateView):
    model = TestModel
    template_name = 'registration/login.html'
    fields = ['name', 'description']
    success_url = '/'