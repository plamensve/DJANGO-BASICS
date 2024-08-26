from django.shortcuts import render

from world_of_speed.profilee.models import Profile


def index(request):
    profile = Profile.objects.first()

    return render(request, 'index.html')


def profile_context_processor(request):

    profile = Profile.objects.first()

    return {'profile': profile}
