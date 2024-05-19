from django.urls import path
from goods import api_views


app_name = 'goods'


urlpatterns = [
    path('products/', api_views.products_list, name='products-list'),
    path('products/<int:pk>/', api_views.retrieve_product, name='retrieve-product'),
    path('products/<int:pk>/partupdate/', api_views.partial_update_product, name='partial_update_product'),
    path('products/<int:pk>/delete/', api_views.delete_product, name='delete_product'),
    path('products/<int:pk>/update/', api_views.update_product, name='update-product'),
    path('products/create/', api_views.create_product, name='create-product'),
]
