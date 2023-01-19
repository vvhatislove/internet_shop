from django.shortcuts import render
from django.views import generic

from cart.cart import Cart
from order.forms import OrderCreateForm
from order.models import OrderItem, Order


# Create your views here.


class OrderCreate(generic.View):

    def get(self, *args, **kwargs):
        cart = Cart(self.request)
        form = OrderCreateForm

        return render(self.request, 'order/create.html',
                      {'cart': cart, 'form': form})

    def post(self, *args, **kwargs):
        cart = Cart(self.request)
        if not len(cart):
            return render(self.request, 'order/created_error.html')
        form = OrderCreateForm(self.request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if self.request.user.is_authenticated:
                order.user = self.request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(self.request, 'order/created.html',
                          {'order': order})


class OrderHistory(generic.ListView):
    model = Order
    template_name = 'order/order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Order.objects.filter(user__pk=self.request.user.pk)
        return orders

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        items = OrderItem.objects.filter(order__user__pk=self.request.user.pk)
        context['items'] = items
        return context
