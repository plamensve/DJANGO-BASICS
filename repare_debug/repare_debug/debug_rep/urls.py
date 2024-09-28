from django.urls import path

from repare_debug.debug_rep.views import index

urlpatterns = [
    path('', index, name='index')
]