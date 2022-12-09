from django.contrib.auth.decorators import login_required
from django.urls import path

from order.views import OrderCreate, OrderHistory

urlpatterns = [
    path('create/', OrderCreate.as_view(), name='order_create'),
    path('order_history/', login_required(OrderHistory.as_view()), name='order_history')
]
