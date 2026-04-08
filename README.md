# Petite Inquieta Shop

E-commerce desarrollado con Django y Python como proyecto final del bootcamp Full Stack Python.

---

## Descripción

Aplicación web que simula una tienda online para **Petite Inquieta**, una marca de cerámica, accesorios e ilustraciones. Incluye un sistema completo de autenticación, catálogo de productos, carrito de compras y gestión de órdenes.

---

## Funcionalidades

- Registro, login y logout de usuarios
- Vista protegida para usuarios autenticados
- Catálogo de productos con filtro por categoría
- Modal para ver imágenes de productos en detalle
- Carrito de compras funcional (agregar, quitar, actualizar cantidades)
- Subtotales y total en tiempo real
- Confirmación y registro de órdenes asociadas al usuario
- Panel de cuenta con historial de pedidos
- CRUD de productos exclusivo para administradores
- Navegación dinámica según estado de autenticación
- Diseño responsive con navbar hamburguesa en mobile

---

## Tecnologías utilizadas

- Python 3
- Django
- HTML5 + CSS3
- Bootstrap 5
- SQLite
- Google Fonts (Playfair Display + Nunito)

---

## Estructura general del proyecto

```text
ecommerce_M6/
├── venv/
└── petite_inquieta_shop/
    ├── manage.py
    ├── static/
    │   ├── css/
    │   │   └── styles.css
    │   └── img/
    │       └── logo.png
    ├── templates/
    │   ├── base.html
    │   ├── inicio.html
    │   ├── productos.html
    │   ├── carrito.html
    │   ├── confirmar_compra.html
    │   ├── registro.html
    │   ├── login.html
    │   ├── mi_cuenta.html
    │   └── partials/
    │       └── navbar.html
    ├── tienda/
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── forms.py
    │   ├── context_processors.py
    │   └── ...
    └── petite_inquieta_shop/
        ├── settings.py
        ├── urls.py
        └── ...
```

---

## Instalación y uso

```bash
# Clonar el repositorio
git clone https://github.com/lissette-dev/petite_inquieta_shop.git

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # En Windows
# source venv/bin/activate  # En Mac/Linux

# Instalar dependencias
pip install django

# Aplicar migraciones
python manage.py migrate

# Crear superusuario (admin)
python manage.py createsuperuser

# Correr el servidor
python manage.py runserver
```

---

## Autora

**Lissette Cornejo** — [github.com/lissette-dev](https://github.com/lissette-dev)