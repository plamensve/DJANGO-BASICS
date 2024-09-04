from django.views import generic as views

from web.forms import IndexForm
from web.models import TruckRoots


# def index(request):
#     form = IndexForm(request.POST or None)
#
#     return form


# class ClassBaseViewIndex(views.TemplateView, views.View):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         if 'form' not in context:
#             context['form'] = IndexForm()
#
#         return context
#
#     def post(self, request, *args, **kwargs):
#         form = IndexForm(request.POST)
#         if form.is_valid():
#
#             return self.render_to_response(self.get_context_data(form=form))

class ToDoCreateForm(views.CreateView):
    model = TruckRoots
    fields = '__all__'
    template_name = 'index.html'
