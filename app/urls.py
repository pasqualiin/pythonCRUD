from django.urls import path, include
from .views import ClienteCreateView, ClienteListView, ClienteUpdateView, ClienteDetailView, ClienteDeleteView


urlpatterns = [
    path("form_clientes", ClienteCreateView.as_view()),
    path("lista_clientes", ClienteListView.as_view(), name="lista_clientes"),
    path("form_clientes/<int:pk>",
         ClienteUpdateView.as_view(), name="edita_clientes"),
    path("detalha_clientes/<int:pk>",
         ClienteDetailView.as_view(), name="detalha_clientes"),
    path("remover_cliente/<int:pk>",
         ClienteDeleteView.as_view(), name="remove_clientes"),
]
