from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:

    def __init__(self, request):
        self._session = request.session
        cart = self._session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self._session[settings.CART_SESSION_ID] = {}
        self._cart = cart

    def __iter__(self):
        product_ids = self._cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self._cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self._cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self._cart:
            self._cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self._cart[product_id]['quantity'] = quantity
        else:
            self._cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self._session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self._cart:
            del self._cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self._cart.values())

    def clear(self):
        del self._session[settings.CART_SESSION_ID]
        self.save()