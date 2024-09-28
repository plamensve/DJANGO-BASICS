from django.shortcuts import render
from repare_debug.debug_rep.forms import PersonForm


def index(request):

    context = {
        'form': PersonForm()
    }

    a = 5
    return render(request, 'base.html', context)
