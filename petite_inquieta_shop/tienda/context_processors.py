from .models import Orden

def carrito_count(request):
    count = 0
    if request.user.is_authenticated:
        orden = Orden.objects.filter(
            usuario=request.user,
            estado='pendiente'
        ).first()
        if orden:
            count = orden.items.count()
    return {'carrito_count': count}