from .serializers import ProductSerializer, CategorySerializer, CategoryDetailSerializer, BrandSerializer, BrandDetailSerializer
from .models import Product, Category, Brand
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

"""
#f
@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()[:10]
    data = ProductSerializer(products, many=True).data
    return Response({'Success':True, 'Product List':data})


@api_view(['GET'])
def product_detail_api(request, id):
    product = Product.objects.get(id=id)
    data = ProductSerializer(product).data
    return Response({'Success':True, 'Product Detail':data})
"""

#cbv
class ProductListApi(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAuthenticated]
    

class ProductDetailApi(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    
    
class CategoryListApi(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    

class CategoryDetailApi(generics.RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    
    
class BrandListApi(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [IsAuthenticated]
    

class BrandDetailApi(generics.RetrieveAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all()
    permission_classes = [IsAuthenticated]

#viewsets
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

#CreateAPIView
#DestroyAPIView
#UpdateAPIView
#ListAPIView
#RetrieveAPIView
#ListCreateAPIView
#RetrieveUpdateAPIView
#RetrieveDestroyAPIView
#RetrieveUpdateDestroyAPIView
