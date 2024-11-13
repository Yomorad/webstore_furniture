from rest_framework import serializers

from goods.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        # fields = [
        #     'name',
        #     'slug',
        #     'description',
        #     'price',
        #     'quantity',
        #     'category',
        # ]
        fields = '__all__'
