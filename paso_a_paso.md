# Paso a paso del desarrollo
## Proyecto final Módulo 6 — Petite Inquieta Shop

Este documento deja respaldo del proceso seguido para construir el proyecto **Petite Inquieta Shop**, una aplicación web en Django con apariencia de e-commerce, enfocada en la implementación de autenticación de usuarios, vistas protegidas y navegación dinámica.

---

## 1. Crear carpeta principal del proyecto

Se trabajó dentro de una carpeta general llamada:

```text
ecommerce_M6
```

---

## 2. Crear y activar entorno virtual

Desde la terminal, en la carpeta `ecommerce_M6`, se ejecutó:

```bash
py -m venv venv
```

Luego se activó el entorno virtual:

```bash
venv\Scripts\activate
```

---

## 3. Actualizar pip

```bash
python -m pip install --upgrade pip
```

---

## 4. Instalar Django

```bash
pip install django
```

---

## 5. Crear el proyecto Django

Se creó el proyecto con el nombre:

```bash
django-admin startproject petite_inquieta_shop
```

Luego se ingresó a la carpeta del proyecto:

```bash
cd petite_inquieta_shop
```

---

## 6. Crear la aplicación principal

Se creó una app llamada `tienda`:

```bash
python manage.py startapp tienda
```

---

## 7. Registrar la app en `settings.py`

En el archivo:

```text
petite_inquieta_shop/settings.py
```

se agregó `'tienda'` en `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tienda',
]
```

---

## 8. Configurar la carpeta de templates

En `settings.py`, dentro de `TEMPLATES`, se modificó la línea:

```python
'DIRS': [],
```

por:

```python
'DIRS': [BASE_DIR / 'templates'],
```

Quedando así:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

---

## 9. Ejecutar migraciones iniciales

```bash
python manage.py migrate
```

---

## 10. Crear archivo de URLs de la app

Dentro de `tienda`, se creó el archivo:

```text
tienda/urls.py
```

con este contenido inicial:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
```

---

## 11. Conectar las URLs de la app con las del proyecto

En:

```text
petite_inquieta_shop/urls.py
```

se dejó:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls')),
]
```

---

## 12. Crear una vista inicial de prueba

En `tienda/views.py` se creó la vista `inicio`.

Primero se hizo una prueba con `HttpResponse`, y luego se cambió para usar template:

```python
from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')
```

---

## 13. Crear la carpeta `templates`

Al mismo nivel de `manage.py`, se creó la carpeta:

```text
templates
```

y dentro de ella el archivo:

```text
inicio.html
```

Contenido inicial:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Petite Inquieta</title>
</head>
<body>
    <h1>Petite Inquieta</h1>
    <p>Piezas de cerámica e ilustraciones inspiradas en lo cotidiano, lo sensible y lo imperfecto.</p>
</body>
</html>
```

---

## 14. Crear template base

Se creó el archivo:

```text
templates/base.html
```

con la estructura base del sitio:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Petite Inquieta{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Petite Inquieta</h1>
        {% include "partials/navbar.html" %}
    </header>

    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>
```

---

## 15. Crear carpeta `partials` y `navbar.html`

Dentro de `templates`, se creó:

```text
templates/partials/navbar.html
```

Contenido inicial:

```html
<nav>
    <a href="{% url 'inicio' %}">Inicio</a>
    <a href="#">Productos</a>
    <a href="#">Login</a>
    <a href="#">Registro</a>
</nav>
<hr>
```

---

## 16. Modificar `inicio.html` para que herede de `base.html`

```html
{% extends "base.html" %}

{% block title %}Inicio | Petite Inquieta{% endblock %}

{% block content %}
    <h2>Bienvenida a Petite Inquieta</h2>
    <p>Piezas de cerámica e ilustraciones inspiradas en lo cotidiano, lo sensible y lo imperfecto.</p>
{% endblock %}
```

---

## 17. Crear vista y template de registro

En `tienda/views.py` se agregó:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = UserCreationForm()

    return render(request, 'registro.html', {'formulario': formulario})
```

En `tienda/urls.py` se agregó la ruta:

```python
path('registro/', views.registro, name='registro'),
```

Se creó el template:

```text
templates/registro.html
```

con el contenido:

```html
{% extends "base.html" %}

{% block title %}Registro | Petite Inquieta{% endblock %}

{% block content %}
    <h2>Crear cuenta</h2>
    <p>Regístrate para acceder a tu espacio en Petite Inquieta.</p>

    <form method="post">
        {% csrf_token %}
        {{ formulario.as_p }}
        <button type="submit">Registrarse</button>
    </form>
{% endblock %}
```

Y se actualizó el navbar para enlazar la ruta real:

```html
<nav>
    <a href="{% url 'inicio' %}">Inicio</a>
    <a href="#">Productos</a>
    <a href="#">Login</a>
    <a href="{% url 'registro' %}">Registro</a>
</nav>
<hr>
```

---

## 18. Crear login y logout

En `tienda/urls.py` se importaron las vistas de autenticación de Django:

```python
from django.contrib.auth.views import LoginView, LogoutView
```

Y se agregaron las rutas:

```python
path('login/', LoginView.as_view(template_name='login.html'), name='login'),
path('logout/', LogoutView.as_view(), name='logout'),
```

Se creó el template:

```text
templates/login.html
```

con el contenido:

```html
{% extends "base.html" %}

{% block title %}Login | Petite Inquieta{% endblock %}

{% block content %}
    <h2>Iniciar sesión</h2>
    <p>Ingresa con tu cuenta para acceder a tu espacio en Petite Inquieta.</p>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Ingresar</button>
    </form>
{% endblock %}
```

---

## 19. Configurar redirecciones de autenticación

En `settings.py` se agregaron:

```python
LOGIN_REDIRECT_URL = '/mi-cuenta/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
```

---

## 20. Crear vista protegida `mi_cuenta`

En `tienda/views.py` se importó:

```python
from django.contrib.auth.decorators import login_required
```

Y se agregó la vista protegida:

```python
@login_required
def mi_cuenta(request):
    return render(request, 'mi_cuenta.html')
```

En `tienda/urls.py` se agregó la ruta:

```python
path('mi-cuenta/', views.mi_cuenta, name='mi_cuenta'),
```

Se creó el template:

```text
templates/mi_cuenta.html
```

con el contenido:

```html
{% extends "base.html" %}

{% block title %}Mi cuenta | Petite Inquieta{% endblock %}

{% block content %}
    <h2>Mi cuenta</h2>
    <p>Bienvenida, {{ user.username }}.</p>
    <p>Esta es una vista protegida, disponible solo para usuarios autenticados.</p>
{% endblock %}
```

---

## 21. Convertir el navbar en dinámico

Se modificó `templates/partials/navbar.html` para que cambie según si el usuario está autenticado o no:

```html
<nav>
    <a href="{% url 'inicio' %}">Inicio</a>
    <a href="{% url 'productos' %}">Productos</a>

    {% if user.is_authenticated %}
        <a href="{% url 'mi_cuenta' %}">Mi cuenta</a>

        <form method="post" action="{% url 'logout' %}" style="display:inline;">
            {% csrf_token %}
            <button type="submit">Logout</button>
        </form>
    {% else %}
        <a href="{% url 'login' %}">Login</a>
        <a href="{% url 'registro' %}">Registro</a>
    {% endif %}
</nav>
<hr>
```

Con esto:
- si el usuario no ha iniciado sesión, ve `Login` y `Registro`
- si ya inició sesión, ve `Mi cuenta` y `Logout`

---

## 22. Crear la página de productos

En `tienda/views.py` se agregó:

```python
def productos(request):
    return render(request, 'productos.html')
```

En `tienda/urls.py` se agregó:

```python
path('productos/', views.productos, name='productos'),
```

Se creó el archivo:

```text
templates/productos.html
```

con el siguiente contenido:

```html
{% extends "base.html" %}

{% block title %}Productos | Petite Inquieta{% endblock %}

{% block content %}
    <h2>Productos</h2>
    <p>Explora las categorías iniciales de Petite Inquieta.</p>

    <section>
        <h3>Accesorios</h3>
        <p>Aros artesanales hechos a mano, pensados para acompañar lo cotidiano con un toque delicado.</p>
    </section>

    <section>
        <h3>Piezas decorativas</h3>
        <p>Porta vela de cerámica para crear espacios cálidos y sensibles.</p>
    </section>

    <section>
        <h3>Ilustraciones</h3>
        <p>Ilustración de gato inspirada en lo simple, lo íntimo y lo imperfecto.</p>
    </section>
{% endblock %}
```

---

## 23. Crear carpeta de archivos estáticos

Al mismo nivel de `manage.py`, se creó la estructura:

```text
static/
└── css/
    └── styles.css
```

En `settings.py` se agregó:

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

---

## 24. Cargar CSS en `base.html`

Se modificó `base.html` para cargar el archivo CSS:

```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Petite Inquieta{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <header class="site-header">
        <div class="contenedor">
            <h1 class="logo">Petite Inquieta</h1>
            {% include "partials/navbar.html" %}
        </div>
    </header>

    <main class="contenedor">
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>
```

---

## 25. Agregar estilos en `styles.css`

Se incorporó un estilo visual inicial para darle una apariencia más cálida y artesanal al sitio:

```css
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background-color: #f8f4ef;
    color: #3d312c;
}

.contenedor {
    width: 90%;
    max-width: 1000px;
    margin: 0 auto;
}

.site-header {
    background-color: #e8ddd1;
    padding: 20px 0;
    border-bottom: 1px solid #d2c2b4;
    margin-bottom: 30px;
}

.logo {
    margin: 0 0 15px 0;
    font-size: 2rem;
    text-align: center;
}

.navbar {
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
}

.navbar a {
    text-decoration: none;
    color: #3d312c;
    font-weight: bold;
}

.navbar a:hover {
    color: #8b5e3c;
}

.logout-form {
    display: inline;
}

.logout-form button {
    background: none;
    border: none;
    color: #3d312c;
    font-weight: bold;
    cursor: pointer;
    padding: 0;
    font-size: 1rem;
}

.logout-form button:hover {
    color: #8b5e3c;
}

main {
    padding-bottom: 40px;
}

section {
    background-color: #fffaf5;
    border: 1px solid #e2d6ca;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
}

h2, h3 {
    color: #5c4438;
}
```

---

## 26. Mejorar la portada con categorías visuales

Se actualizó `inicio.html` para que la portada se pareciera más a una tienda y presentara las categorías principales.

Contenido:

```html
{% extends "base.html" %}

{% block title %}Inicio | Petite Inquieta{% endblock %}

{% block content %}
    <section>
        <h2>Bienvenida a Petite Inquieta</h2>
        <p>Piezas de cerámica e ilustraciones inspiradas en lo cotidiano, lo sensible y lo imperfecto.</p>

        <p>
            <a href="{% url 'productos' %}">Ver productos</a>
            {% if not user.is_authenticated %}
                | <a href="{% url 'registro' %}">Crear cuenta</a>
            {% endif %}
        </p>
    </section>

    <section>
        <h3>Explora nuestras categorías</h3>

        <div class="tarjetas">
            <article class="tarjeta">
                <h4>Accesorios</h4>
                <p>Piezas delicadas para acompañar tu día a día.</p>
            </article>

            <article class="tarjeta">
                <h4>Piezas decorativas</h4>
                <p>Objetos de cerámica para espacios cálidos y sensibles.</p>
            </article>

            <article class="tarjeta">
                <h4>Ilustraciones</h4>
                <p>Imágenes pensadas desde lo íntimo, lo simple y lo imperfecto.</p>
            </article>
        </div>
    </section>
{% endblock %}
```

Y al final de `styles.css` se agregaron:

```css
.tarjetas {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 20px;
}

.tarjeta {
    background-color: #fffaf5;
    border: 1px solid #e2d6ca;
    border-radius: 10px;
    padding: 20px;
    flex: 1 1 250px;
    box-sizing: border-box;
}

.tarjeta h4 {
    margin-top: 0;
    color: #5c4438;
}
```

---

## 27. Probar el flujo completo de autenticación

Se comprobó el funcionamiento del sistema:

### Registro
- Se ingresó a `/registro/`
- Se creó un usuario con `UserCreationForm`

### Login
- Luego del registro, se redirigió a `/login/`
- Se inició sesión correctamente

### Vista protegida
- Tras iniciar sesión, el usuario fue redirigido a `/mi-cuenta/`
- Se confirmó que la vista solo era accesible si el usuario estaba autenticado

### Logout
- Se probó el cierre de sesión desde el navbar
- Al cerrar sesión, el usuario volvió al inicio
- Si intentaba volver a `/mi-cuenta/`, era redirigido a `/login/`

---

## 28. Rutas principales del proyecto

- `/` → Inicio
- `/productos/` → Productos
- `/registro/` → Registro
- `/login/` → Inicio de sesión
- `/logout/` → Cierre de sesión
- `/mi-cuenta/` → Vista protegida

---

## 29. Ejecución del proyecto

Con el entorno virtual activado y dentro de la carpeta donde está `manage.py`, se ejecuta:

```bash
python manage.py runserver
```

Luego se abre en el navegador:

```text
http://127.0.0.1:8000/
```

---

## 30. Resultado final alcanzado

Se desarrolló una aplicación funcional con:

- autenticación de usuarios
- registro
- login
- logout
- vista protegida
- templates reutilizables
- navbar dinámica
- página de productos
- estilo visual inicial con identidad de tienda

Además, el proyecto quedó planteado como una base real para seguir desarrollando a futuro el e-commerce de **Petite Inquieta**.