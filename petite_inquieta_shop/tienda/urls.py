from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # --- Vistas Públicas ---
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # --- Vistas Protegidas ---
    path('mi-cuenta/', views.mi_cuenta, name='mi_cuenta'),

    # --- CRUD de productos ---
    path('products/create/', views.producto_create, name='producto_create'),
    path('products/edit/<int:pk>/', views.producto_edit, name='producto_edit'),
    path('products/delete/<int:pk>/', views.producto_delete, name='producto_delete'),

    # --- Carrito ---
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/quitar/<int:item_id>/', views.quitar_del_carrito, name='quitar_del_carrito'),
    path('carrito/actualizar/<int:item_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('carrito/confirmar/', views.confirmar_compra, name='confirmar_compra'),
]