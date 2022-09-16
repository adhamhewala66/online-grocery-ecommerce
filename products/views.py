from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Brand, Category

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class BrandList(ListView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorys"] = Category.objects.all()
        return context

class BrandDetail(DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brand_products"] = Product.objects.filter(brand=brand)
        return context
    
class CategoryList(ListView):
    model = Category
