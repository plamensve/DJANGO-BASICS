from django.urls import path

from petstagram_ws1.common.views import index

urlpatterns = [
    path('', index, name='index')
]