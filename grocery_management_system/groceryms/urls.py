from django.urls import path
from .views import CategoryList, ProductList, SaleList

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('categories/', CategoryList.as_view(), name='category_list'),
#     path('products/', ProductList.as_view(), name='product_list'),
#     path('sales/', SaleList.as_view(), name='sale_list'),
# ]

urlpatterns = [
    path('', CategoryList.as_view(), name='category_list'),  # Update this line if you want to load the category list on the home page
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('products/', ProductList.as_view(), name='product_list'),
    path('sales/', SaleList.as_view(), name='sale_list'),
]
