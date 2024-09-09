

from django.urls import path
from main.views import IndexView, ClienteCreateView, ClienteListView

urlpatterns = [
    path('test/', IndexView.as_view(), name='test'),
    path('cliente/add/', ClienteCreateView.as_view(), name='cliente_add'),
    path('cliente/success/', ClienteCreateView.as_view(template_name='cliente_success.html'), name='cliente_success'),
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
]
