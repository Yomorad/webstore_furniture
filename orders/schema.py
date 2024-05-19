import graphene
from graphene_django.types import DjangoObjectType
from orders.models import Order, OrderItem

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
class OrderItemType(DjangoObjectType):
    class Meta:
        model = OrderItem
class Query(graphene.ObjectType):
    """ Описываем запросы и возвращаемые типы данных """
    order_list = graphene.List(OrderType)
    orderitem_list = graphene.List(OrderItemType)

    def resolve_order_list(self, info, **kwargs):
        return Order.objects.all()

    def resolve_orderitem_list(self, info, **kwargs):
        return OrderItem.objects.all()

schema = graphene.Schema(query=Query)