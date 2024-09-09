from django.shortcuts import render



from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import ClienteForm
from django.views.generic import ListView
from .models import Cliente

class IndexView(TemplateView):
    template_name = 'test.html'
    

class ClienteCreateView(FormView):
    template_name = 'cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_success')

    def form_valid(self, form):
        form.save()  
        return super().form_valid(form)
    

    
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'


