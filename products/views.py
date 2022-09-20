from ast import For
from itertools import count
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Brand, Category
from django.db.models import Q, F, Value
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Sum, Avg

def product_list(request):
    products = Product.objects.all()
    
    #products = Product.objects.filter(price__gt=30)#__gt, __gte, __lt, __lte
    #products = Product.objects.filter(price__range=(30,60))
    #products = Product.objects.filter(category__id=8)
    #products = Product.objects.filter(category__id__gt=8)
    #products = Product.objects.filter(name__contains='th')
    #products = Product.objects.filter(name__startswith='th')
    #products = Product.objects.filter(name__endswith='on')
    #products = Product.objects.filter(name__endswith='on', quantity__gt=80)#combine>>AND
    '''
    products = Product.objects.filter(
        Q(name__endswith='on') | Q(quantity__gt=80)
    )#combine>>OR, in Q object we can use &, |, ~
    
    products = Product.objects.filter(
        Q(name__endswith='on') | ~Q(quantity__gt=80)
    )#combine>>ends | ~__gt
    '''
    #products = Product.objects.filter(quantity=F('price'))#two columns are equal
    
    #products = Product.objects.order_by('name')#ASC
    #products = Product.objects.order_by('-name')#DESC
    #products = Product.objects.order_by('name', 'price')
    #products = Product.objects.filter(price__range=(30,60)).order_by('name')
    
    #products = Product.objects.earliest('name')#don't use loop in its html just {{products}}
    #products = Product.objects.latest('name')#don't use loop in its html just {{products}}
    
    #products = Product.objects.all()[:10]#slicing 0=>9
    
    #products = Product.objects.all()#return only name&price as in html but will return all columns in sql debug toolbar
    #products = Product.objects.values('name', 'price')#return name&price in dictionary but will return just name&price columns in sql debug toolbar
    #products = Product.objects.values_list('name', 'price', 'category__name', 'brand__name')
    
    #products = Product.objects.only('name')#make sure that there is only name field in html or queryset will run for 200ms
    #products = Product.objects.all()#and put {{product.category}} in loop in html=>this will make queryset still run for long
    #products = Product.objects.select_related('category').all()#here query will run so faster cause it make join with category
    #the same if we add brand:
    #products = Product.objects.all()#false
    #products = Product.objects.select_related('category').select_related('brand').all()#true
    #we use this in case relations is one-to-one or one-to-many
    #but in case relations is many-to-many we use prefetch_related
    
    #Aggregation functions(there isn't loop in html):
    #products = Product.objects.aggregate(Count('quantity'))#here it returns count but no recurrision
    #products = Product.objects.aggregate(Sum('quantity'))#here will return the absolute number of qty
    #products = Product.objects.aggregate(Min('price')
    #products = Product.objects.aggregate(Max('price'))
    #products = Product.objects.aggregate(Avg('price'))
    #products = Product.objects.aggregate(myAvg = Avg('quantity'), myMax = Max('price'))
    
    #products = Product.objects.annotate(is_new=Value(True))#create new column has value true (in sql debug setion)
    #products = Product.objects.annotate(info=Concat('name', 'flag'))#a new column consists of name + flag (concatenated)
    
    return render(request, 'products/product_list_test.html', context={'products':products})

class ProductList(ListView):
    model = Product
    paginate_by = 100

class ProductDetail(DetailView):
    model = Product

class BrandList(ListView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorys"] = Category.objects.all()
        context["brand_list"] = Brand.objects.all().annotate(product_count=Count('product_brand'))#calculated field
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
