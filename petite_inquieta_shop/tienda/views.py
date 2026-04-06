from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from functools import wraps
from .models import Producto, Orden, ItemOrden
from .forms import ProductoForm


# --- Decorador personalizado: solo staff/admin ---

def staff_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, 'No tienes permiso para realizar esta acción.')
            return redirect('productos')
        return view_func(request, *args, **kwargs)
    return wrapper


# --- Vistas Públicas ---

def inicio(request):
    return render(request, 'inicio.html')

def productos(request):
    categoria_nombre = request.GET.get('categoria')
    if categoria_nombre:
        lista_productos = Producto.objects.filter(categoria__nombre__iexact=categoria_nombre)
    else:
        lista_productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': lista_productos})

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario registrado con éxito. ¡Ya puedes iniciar sesión!')
            return redirect('login')
    else:
        formulario = UserCreationForm()
    return render(request, 'registro.html', {'formulario': formulario})


# --- Vistas Protegidas ---

@login_required
def mi_cuenta(request):
    return render(request, 'mi_cuenta.html')


# --- CRUD de productos (solo staff/admin) ---

@login_required
@staff_required
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form, 'titulo': 'Agregar Nuevo Producto'})

@login_required
@staff_required
def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado con éxito.')
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form, 'titulo': 'Editar Producto'})

@login_required
@staff_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.warning(request, 'El producto ha sido eliminado.')
        return redirect('productos')
    return render(request, 'producto_confirm_delete.html', {'producto': producto})


# --- Carrito ---

def get_or_create_carrito(request):
    """Función auxiliar: obtiene o crea la orden pendiente del usuario."""
    orden, creada = Orden.objects.get_or_create(
        usuario=request.user,
        estado='pendiente'
    )
    return orden

@login_required
def ver_carrito(request):
    orden = get_or_create_carrito(request)
    return render(request, 'carrito.html', {'orden': orden})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    orden = get_or_create_carrito(request)
    item, creado = ItemOrden.objects.get_or_create(
        orden=orden,
        producto=producto,
        defaults={'precio_unitario': producto.precio}
    )
    if not creado:
        item.cantidad += 1
        item.save()
    messages.success(request, f'"{producto.nombre}" agregado al carrito.')
    return redirect('ver_carrito')

@login_required
def quitar_del_carrito(request, item_id):
    item = get_object_or_404(ItemOrden, id=item_id, orden__usuario=request.user)
    nombre = item.producto.nombre
    item.delete()
    messages.warning(request, f'"{nombre}" eliminado del carrito.')
    return redirect('ver_carrito')

@login_required
def actualizar_cantidad(request, item_id):
    item = get_object_or_404(ItemOrden, id=item_id, orden__usuario=request.user)
    nueva_cantidad = int(request.POST.get('cantidad', 1))
    if nueva_cantidad < 1:
        item.delete()
        messages.warning(request, 'Producto eliminado del carrito.')
    else:
        item.cantidad = nueva_cantidad
        item.save()
        messages.success(request, 'Cantidad actualizada.')
    return redirect('ver_carrito')

@login_required
def confirmar_compra(request):
    orden = get_or_create_carrito(request)
    if not orden.items.exists():
        messages.warning(request, 'Tu carrito está vacío.')
        return redirect('ver_carrito')
    if request.method == 'POST':
        orden.estado = 'confirmada'
        orden.save()
        messages.success(request, f'¡Compra confirmada! Orden #{orden.id} registrada.')
        return redirect('mi_cuenta')
    return render(request, 'confirmar_compra.html', {'orden': orden})