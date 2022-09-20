from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail, CategoryList, product_list
from .api import ProductList, ProductDetail

app_name = 'products'
urlpatterns = [
    path('testing/', product_list),
    path('', ProductList.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('brands/', BrandList.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetail.as_view(), name='brand-detail'),
    path('category/', CategoryList.as_view(), name='category-list'),
    #path('api/list', product_list_api),
    #path('api/list/<int:id>', product_detail_api),
    path('api/list/cbv', ProductList.as_view()),
    path('api/list/cbv/<int:pk>', ProductDetail.as_view()),
]
