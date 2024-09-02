from django.http import HttpResponse
from django.shortcuts import render

from web.forms import IndexForm


def index(request):
    form = IndexForm(request.POST or None)

    context = {
        'form': form
    }

    return render(request, 'index.html', context)