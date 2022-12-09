from django.urls import path
from cart.views import CartDetailView, CartRemoveRedirectView, CartAddRedirectView


urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', CartAddRedirectView.as_view(), name='cart_add'),
    path('remove/<int:product_id>/', CartRemoveRedirectView.as_view(), name='cart_remove'),
]
