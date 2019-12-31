from decimal import Decimal
from django.conf import settings
from inicio.models import Juguete


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, juguete, cantidad=1, update_cantidad=False):
        juguete_id = str(juguete.id)
        if juguete_id not in self.cart:
            self.cart[juguete_id] = {'cantidad': 0, 'precio': str(juguete.precio)}
        if update_cantidad:
            self.cart[juguete_id]['cantidad'] = cantidad
        else:
            self.cart[juguete_id]['cantidad'] += cantidad
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, juguete):
        juguete_id = str(juguete.id)
        if juguete_id in self.cart:
            del self.cart[juguete_id]
            self.save()

    def __iter__(self):
        juguete_ids = self.cart.keys()
        juguetes = Juguete.objects.filter(id__in=juguete_ids)
        for juguete in juguetes:
            self.cart[str(juguete.id)]['juguete'] = juguete

        for item in self.cart.values():
            item['precio'] = Decimal(item['precio'])
            item['total_precio'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        return sum(item['cantidad'] for item in self.cart.values())

    def get_total_precio(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True