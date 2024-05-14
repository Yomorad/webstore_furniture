from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render


from goods.models import Products
from goods.utils import q_search

from django.views.decorators.cache import cache_page

from django_app.serializers import ProductsSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
# Create your views here.

@cache_page(60)
def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        'title' : 'Home - Каталог',
        'goods' : current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)

@cache_page(60)
def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context=context)



@api_view(['GET'])
def products_list(request):
    queryset = Products.objects.all()
    serializer = ProductsSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_product(request, pk):
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductsSerializer(product)
    return Response(serializer.data)

@api_view(['PUT'])
def update_product(request, pk):
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductsSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def partial_update_product(request, pk):
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductsSerializer(instance=product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Products.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)