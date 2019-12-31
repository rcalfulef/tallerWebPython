from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from inicio.models import Juguete
from .cart import Cart
from .forms import CartAddJugueteForm


@require_POST
def cart_add(request, juguete_id):
    
    cart = Cart(request)
    juguete = get_object_or_404(Juguete, id=juguete_id)
    form = CartAddJugueteForm(request.POST)
    if form.is_valid():
        print("se entra")
        cd = form.cleaned_data
        cart.add(juguete=juguete, cantidad=cd['cantidad'], update_cantidad=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, juguete_id):
    cart = Cart(request)
    juguete = get_object_or_404(Juguete, id=juguete_id)
    cart.remove(juguete)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_cantidad_form'] = CartAddJugueteForm(initial={'cantidad': item['cantidad'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})