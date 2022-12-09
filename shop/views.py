from django.shortcuts import get_object_or_404
from django.views import generic

from cart.forms import CartAddProductForm
from shop.models import Product, Category


# Create your views here.


class HomeView(generic.ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            return Product.objects.filter(category__slug=category_slug, available=True)
        return Product.objects.filter(available=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = None
        categories = Category.objects.all()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
        context['categories'] = categories
        context['category'] = category
        return context


class ProductView(generic.ListView):
    model = Product
    template_name = 'shop/product.html'
    context_object_name = 'product'

    def get_queryset(self):
        product = get_object_or_404(Product, slug=self.kwargs.get('product_slug'), available=True)
        return product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context
