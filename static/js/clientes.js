
document.addEventListener('DOMContentLoaded', () => {
    // CONFIRMACIÓN DE CAMBIO DE ESTADO
    document.querySelectorAll('.form-cambiar-estado').forEach(formulario => {
        formulario.addEventListener('submit', async (event) => {
            event.preventDefault();

            const nombre = formulario.dataset.nombre;
            const accion = formulario.dataset.accion;
            const inactivar = accion === 'inactivar';

            const resultado = await Swal.fire({
                title: inactivar ? '¿Inactivar cliente?' : '¿Activar cliente?',
                text: `¿Estás seguro de ${accion} a ${nombre}?`,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Sí, confirmar',
                cancelButtonText: 'Cancelar',
                buttonsStyling: false,
                customClass: {
                    confirmButton: inactivar
                        ? 'btn btn-danger mx-2'
                        : 'btn btn-success mx-2',
                    cancelButton: 'btn btn-secondary mx-2'
                },
                reverseButtons: true
            });

            if (resultado.isConfirmed) {
                formulario.submit();
            }
        });
    });
});
