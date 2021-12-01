from pos.models import Order, OrderItem, OrderItemTopping
from rest_framework import serializers
from product.serializers import ProductSerializer,ToppingSerializer,SaleChannelSerializer

        

class OrderItemToppingSerializer(serializers.ModelSerializer):
    topping_set =  ToppingSerializer(read_only=True)
    class Meta:
        model = OrderItemTopping
        fields = ['id', 'item', 'topping', 'total_price', 'amount','topping_set']


class OrderItemSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    order_topping_set = OrderItemToppingSerializer(many=True,read_only=True,source="orderitemtopping_set")
    class Meta:
        model = OrderItem
        fields = ['id', 'flavour_level', 'product',
                  'order', 'total_price', 'descriptions', 'amount','product_set','order_topping_set']



class OrderSerializer(serializers.ModelSerializer):
    order_item_set = OrderItemSerializer(many=True,read_only=True,source="orderitem_set")
    class Meta:
        model = Order
        fields = ['id', 'status_delivery', 'total_price', 'total_amount',
          'sale_channel', 'customer_name', 'descriptions', 'status_order','order_item_set']