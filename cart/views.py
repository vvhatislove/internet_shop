from django.shortcuts import get_object_or_404
from django.views import generic

from cart.cart import Cart
from cart.forms import CartAddProductForm
from shop.models import Product


class CartDetailView(generic.TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                       'update': True})
        context['cart'] = cart
        return context


class CartRemoveRedirectView(generic.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'cart_detail'

    def get_redirect_url(self, *args, **kwargs):
        cart = Cart(self.request)
        product = get_object_or_404(Product, id=self.kwargs.get('product_id'))
        cart.remove(product)
        if not len(cart):
            self.pattern_name='home_view'
        return super().get_redirect_url()


class CartAddRedirectView(generic.RedirectView):
    permanent = True
    pattern_name = 'cart_detail'

    def get_redirect_url(self, *args, **kwargs):
        cart = Cart(self.request)
        product = get_object_or_404(Product, id=self.kwargs.get('product_id'))
        form = CartAddProductForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        return super().get_redirect_url()
