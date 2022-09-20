from django.urls import path, include
from .views import ProductList, ProductDetail, BrandList, BrandDetail, CategoryList, product_list
from .api import ProductListApi, ProductDetailApi, CategoryListApi, CategoryDetailApi, BrandListApi, BrandDetailApi, ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('myproducts', ProductViewSet)

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
    path('api/list/cbv/', ProductListApi.as_view()),
    path('api/list/cbv/<int:pk>', ProductDetailApi.as_view()),
    path('api/category', CategoryListApi.as_view()),
    path('api/category/<int:pk>', CategoryDetailApi.as_view()),
    path('api/brand', BrandListApi.as_view()),
    path('api/brand/<int:pk>', BrandDetailApi.as_view()),
    path('myapi/', include(router.urls))
]
