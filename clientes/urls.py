from django.urls import path

from . import views

urlpatterns = [
    path('', views.crear_cliente, name='clientes_crear'),
    path('<int:cliente_id>/editar/', views.editar_cliente, name='clientes_editar'),
    path('<int:cliente_id>/estado/', views.cambiar_estado_cliente, name='clientes_estado'),
]