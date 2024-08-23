from django.urls import path

from templates_advanced.main_app.views import index

urlpatterns = (
    path('', index, name='index'),
)
