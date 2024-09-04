from django.urls import path

from web.views import ToDoCreateForm

urlpatterns = (
    path('', ToDoCreateForm.as_view(), name='index'),
)
