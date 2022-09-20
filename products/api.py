from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework import generics

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
class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
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
