from django.contrib.auth.views import LoginView
from django.urls import path
from django.views.generic import CreateView

from world_of_speed.web.views import index, TestModelCreateView

urlpatterns = (
    path('', index, name='index'),
    path('login/', TestModelCreateView.as_view(template_name='registration/login.html'), name='login')
)