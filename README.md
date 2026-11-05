# DjangoPractica

## Descripción

Proyecto desarrollado para el curso de Desarrollo Web, Módulo III, de la Universidad Mariano Gálvez de Guatemala.

Consiste en una aplicación web creada con Django y conectada a una base de datos MySQL/MariaDB. Permite registrar usuarios, iniciar sesión y administrar clientes mediante una interfaz web.

La aplicación se desarrolló localmente y posteriormente se publicó en Railway para permitir su acceso desde internet.

## Tecnologías utilizadas

- Python 3.13
- Django 6.1.3
- MariaDB 13.0.2 para desarrollo local
- MySQL para el despliegue
- Bootstrap 5
- JavaScript y SweetAlert2
- Gunicorn
- WhiteNoise
- Git y GitHub
- Railway

## Funcionalidades

### Autenticación

- Registro de usuarios.
- Inicio y cierre de sesión.
- Formularios para recuperación de contraseña.
- Restricción de acceso a las páginas de clientes mediante autenticación.

**Nota:** el restablecimiento de contraseñas requiere configurar un servicio de envío de correos para funcionar mediante correo electrónico en producción.

### Gestión de clientes

- Registrar clientes con nombre y correo electrónico.
- Consultar los clientes registrados.
- Editar la información de un cliente.
- Activar e inactivar clientes sin eliminar los registros.
- Confirmar los cambios de estado mediante SweetAlert2.
- Mostrar mensajes de confirmación después de realizar operaciones.

## Estructura del proyecto

```text
DjangoPractica/
├── app/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── forms.py
│   └── wsgi.py
├── clientes/
│   ├── migrations/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── static/
│   ├── img/
│   └── js/
├── templates/
│   ├── clientes/
│   ├── registration/
│   ├── base.html
│   └── home.html
├── .gitignore
├── Procfile
├── manage.py
└── requirements.txt
```

## Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/jeliasc/DjangoPractica.git
cd DjangoPractica
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv
```

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Crear una base de datos MySQL/MariaDB denominada `django_db` y un usuario con permisos sobre ella.

Crear un archivo `.env` en la raíz del proyecto y configurar:

```dotenv
DJANGO_SECRET_KEY=CLAVE_SECRETA_GENERADA
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=django_db
DB_USER=django_user
DB_PASSWORD=CONTRASEÑA_LOCAL
DB_HOST=127.0.0.1
DB_PORT=3306
```

Los valores deben adaptarse a la instalación local. El archivo `.env` no debe publicarse en GitHub.

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

Acceder a:

http://127.0.0.1:8000/

## Despliegue en Railway

La aplicación se publicó en Railway utilizando dos servicios:

- **web:** ejecuta Django mediante Gunicorn.
- **MySQL:** almacena los usuarios, sesiones y clientes.

La configuración se realiza mediante variables de entorno para evitar publicar contraseñas en el repositorio.

**Comando de compilación:**

```bash
python manage.py collectstatic --noinput
```

**Comando previo al despliegue:**

```bash
python manage.py migrate --noinput
```

**Comando de inicio:**

```bash
gunicorn app.wsgi:application --bind 0.0.0.0:$PORT
```

Las variables `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER` y `DB_PASSWORD` se configuran mediante referencias al servicio MySQL de Railway.

También se configuran `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, `DJANGO_ALLOWED_HOSTS` y `DJANGO_CSRF_TRUSTED_ORIGINS`.

## Enlaces

**Aplicación publicada:**

https://web-production-d011e.up.railway.app/

**Repositorio GitHub:**

https://github.com/jeliasc/DjangoPractica

## Estado del proyecto

La aplicación fue desplegada en Railway con conexión a MySQL. Se verificaron el acceso público, la autenticación y el registro y listado de clientes.

Las funcionalidades de edición y cambio de estado fueron probadas en el entorno local; su validación final en producción queda pendiente de documentar.