````markdown
# Petite Inquieta Shop - PARTE I

Proyecto final del **Módulo 6 – Desarrollo de Aplicaciones Web con Python Django**.

Este proyecto consiste en una aplicación web desarrollada con Django que simula un e-commerce para **Petite Inquieta**, una tienda de cerámica e ilustración. Su objetivo principal es implementar un sistema de autenticación de usuarios con **registro, login, logout y vista protegida**, además de una navegación con templates reutilizables y una apariencia inicial de tienda online.

---

## Descripción del proyecto

La aplicación representa una versión MVP de un e-commerce inspirado en la tienda **Petite Inquieta**, incorporando categorías de productos como:

- Accesorios
- Piezas decorativas
- Ilustraciones

Actualmente, el sitio incluye:

- Página de inicio
- Página de productos
- Registro de usuario
- Inicio de sesión
- Cierre de sesión
- Vista protegida para usuarios autenticados
- Navegación dinámica según estado de autenticación

---

## Tecnologías utilizadas

- Python
- Django
- HTML
- CSS
- SQLite

---

## Estructura general del proyecto
```text
ecommerce_M6/
├── venv/
└── petite_inquieta_shop/
    ├── manage.py
    ├── static/
    │   └── css/
    │       └── styles.css
    ├── templates/
    │   ├── base.html
    │   ├── inicio.html
    │   ├── productos.html
    │   ├── registro.html
    │   ├── login.html
    │   ├── mi_cuenta.html
    │   └── partials/
    │       └── navbar.html
    ├── tienda/
    │   ├── views.py
    │   ├── urls.py
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
git clone https://github.com/lissette-dev/petite-inquieta.git

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install django

# Aplicar migraciones
python manage.py migrate

# Correr el servidor
python manage.py runserver
```

---

## Autora

**Lissette Cornejo** — [github.com/lissette-dev](https://github.com/lissette-dev)
````





