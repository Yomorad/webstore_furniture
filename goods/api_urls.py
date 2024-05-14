from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('products/', views.products_list, name='products-list'),
    path('products/<int:pk>/', views.retrieve_product, name='retrieve-product'),
    path('products/<int:pk>/partupdate/', views.partial_update_product, name='partial_update_product'),
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('products/<int:pk>/update/', views.update_product, name='update-product'),
    path('products/create/', views.create_product, name='create-product'),
]
