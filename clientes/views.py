from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ClienteForm
from .models import Cliente

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            cliente = form.save()
            messages.success(
                request,
                f'Cliente guardado: {cliente.nombre} ({cliente.correo})'
            )
            return redirect('clientes_crear')
    else:
        form = ClienteForm()

    clientes = Cliente.objects.order_by('-id')

    return render(request, 'clientes/create.html', {
        'form': form,
        'clientes': clientes,
    })


@login_required
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado correctamente.')
            return redirect('clientes_crear')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/edit.html', {
        'form': form,
        'cliente': cliente,
    })


@login_required
@require_POST
def cambiar_estado_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    cliente.activo = not cliente.activo
    cliente.save(update_fields=['activo'])

    estado = 'activado' if cliente.activo else 'inactivado'

    messages.success(
        request,
        f'Cliente {estado} correctamente.'
    )

    return redirect('clientes_crear')
