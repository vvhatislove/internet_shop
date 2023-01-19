from django.urls import path

from shop.views import HomeView, ProductView

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('<slug:category_slug>/', HomeView.as_view(), name='category_view'),
    path('<slug:category_slug>/<slug:product_slug>/', ProductView.as_view(), name='product_view'),
]
