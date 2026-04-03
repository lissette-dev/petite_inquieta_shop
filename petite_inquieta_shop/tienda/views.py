from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Requisito: Mensajes de feedback
from .models import Producto
from .forms import ProductoForm # Recuerda crear el archivo forms.py que te pasé antes

# --- Vistas Públicas ---

def inicio(request):
    return render(request, 'inicio.html')

def productos(request):
    # Capturamos si viene una categoría en la URL (ej: ?categoria=Accesorios)
    categoria_nombre = request.GET.get('categoria')
    
    if categoria_nombre:
        # Filtramos los productos que pertenezcan a esa categoría
        lista_productos = Producto.objects.filter(categoria__nombre__iexact=categoria_nombre)
    else:
        # Si no hay filtro, mostramos todo como antes
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

# --- Vistas Protegidas (Solo para usuarios logueados/Admin) ---

@login_required
def mi_cuenta(request):
    return render(request, 'mi_cuenta.html')

# 2. CREAR
@login_required
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('productos') # Te redirige al catálogo
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form, 'titulo': 'Agregar Nuevo Producto'})

# 3. EDITAR
@login_required
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

# 4. ELIMINAR
@login_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.warning(request, 'El producto ha sido eliminado.')
        return redirect('productos')
    return render(request, 'producto_confirm_delete.html', {'producto': producto})