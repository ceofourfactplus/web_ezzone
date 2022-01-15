from django.db.models import Sum, F, Count
from product.models import SaleChannel
from pos.models import Order, OrderItem, OrderItemTopping, Payment
from pos.serializers import OrderSerializer, PaymentSerializer, OrderItemSerializer, OrderItemToppingSerializer
from rest_framework.views import APIView
from customer.models import Customer, AddressCustomer
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from pprint import pprint
from product.models import Product
from product.serializers import ProductReportSerialiser
import datetime


def check_is_finish(order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise 404

    if (order.payment_status == 3 or order.payment_status == 4) and (order.status_food == 2 or order.status_food == None) and (order.status_drink == 2 or order.status_drink == None):
        order.status_order = 3
        order.save()
    serializer = OrderSerializer(order)
    pprint(serializer.data)


class SelectPaymentOrder(APIView):

    def put(self, request, order_id, payment_id):
        orders = Order.objects.get(pk=order_id)
        orders.payment_status = 4
        payment = Payment.objects.get(pk=payment_id)
        print(request.data)
        if payment.payment.upper() == "CASH":
            orders.payment_status = 3
            orders.cash = request.data['cash']
            orders.change = int(float(orders.total_balance)
                                ) - int(request.data['cash'])
        orders.payment_id = payment_id
        orders.save()
        check_is_finish(order_id)
        return Response('ok')


class PaymentList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        Orders = Payment.objects.all()
        serializer = PaymentSerializer(
            Orders, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TodayOrderList(APIView):
    parser_classes = [FormParser, MultiPartParser]

    def get(self, request):
        Orders = Order.objects.filter(
            create_at__gte=datetime.datetime.now().date())
        serializer = OrderSerializer(
            Orders, context={'request': request}, many=True)
        return Response(serializer.data)


class DrinkOrderOnGoing(APIView):
    parser_classes = [FormParser, MultiPartParser]

    def get(self, request):
        Orders = Order.objects.filter(
            create_at__gte=datetime.datetime.now().date(), status_drink__in=[0, 1]).exclude(status_drink=None)
        serializer = OrderSerializer(
            Orders, context={'request': request}, many=True)
        return Response(serializer.data)


class AcceptDrinkOrder(APIView):
    def put(self, request, pk):
        orders = Order.objects.get(pk=pk)
        if not orders.status_food == 0:
            orders.status_order = 1
        orders.status_drink = 1
        orders.save()
        product = [p.id for p in Product.objects.filter(type_product=2)]
        orderitem = OrderItem.objects.filter(
            order_id=pk, product_id__in=product)
        for item in orderitem:
            item.status_order = 1
            item.save()
        return Response('ok')


class FinishDrinkOrderItem(APIView):
    def put(self, request, pk):
        orders = OrderItem.objects.get(pk=pk)
        orders.status_order = 2
        orders.save()
        product = [p.id for p in Product.objects.filter(type_product=2)]
        o = Order.objects.get(pk=orders.order_id)
        if not OrderItem.objects.filter(order_id=o.id, status_order=1, product_id__in=product).exists():
            if (o.status_food == None or o.status_food == 2) and (o.payment_status == 3 or o.payment_status == 4):
                o.status_order = 3
            o.status_drink = 2
            o.save()
        return Response('ok')


class FinishDrinkOrder(APIView):
    def put(self, request, pk):
        orders = Order.objects.get(pk=pk)
        orders.status_drink = 2
        product = [p.id for p in Product.objects.filter(type_product=2)]
        if not OrderItem.objects.filter(order_id=pk, status_order=1, product_id__in=product).exists():
            if (orders.status_food == None or orders.status_food == 2) and (orders.payment_status == 3 or orders.payment_status == 4):
                orders.status_order = 3
        orders.save()

        for o in OrderItem.objects.filter(order_id=orders.id, product_id__in=product):
            o.status_order = 2
            o.save()
        return Response('ok')


class FoodOrderOnGoing(APIView):
    def get(self, request):
        Orders = Order.objects.filter(
            create_at__gte=datetime.datetime.now().date(), status_food__in=[0, 1]).exclude(status_food=None)
        serializer = OrderSerializer(
            Orders, many=True)
        return Response(serializer.data)


class AcceptFoodOrder(APIView):
    def put(self, request, pk):
        orders = Order.objects.get(pk=pk)
        if not orders.status_drink == 0:
            orders.status_order = 1
        orders.status_food = 1
        orders.save()
        orderitem = OrderItem.objects.filter(order_id=pk)
        for item in orderitem:
            item.status_order = 1
            item.save()
        return Response('ok')


class FinishFoodOrderItem(APIView):
    def put(self, request, pk):
        orders = OrderItem.objects.get(pk=pk)
        orders.status_order = 2
        orders.save()
        product = [p.id for p in Product.objects.filter(
            type_product__in=[3, 1])]
        o = Order.objects.get(pk=orders.order_id)
        print(not OrderItem.objects.filter(order_id=o.id,
                                           status_order=1, product_id__in=product).exists())
        if not OrderItem.objects.filter(order_id=o.id, status_order=1, product_id__in=product).exists():
            if (o.status_drink == None or o.status_drink == 2) and (o.payment_status == 3 or o.payment_status == 4):
                o.status_order = 3
                print('in loop')
            o.status_food = 2
            o.save()
        return Response('ok')


class FinishFoodOrder(APIView):
    def put(self, request, pk):
        orders = Order.objects.get(pk=pk)
        orders.status_food = 2
        product = [p.id for p in Product.objects.filter(
            type_product__in=[1, 3])]
        print(not OrderItem.objects.filter(order_id=pk,
                                           status_order=1, product_id__in=product).exists())
        if not OrderItem.objects.filter(order_id=pk, status_order=1, product_id__in=product).exists():
            if (orders.status_drink == None or orders.status_drink == 2) and (orders.payment_status == 3 or orders.payment_status == 4):
                orders.status_order = 3
        orders.save()

        for o in OrderItem.objects.filter(order_id=orders.id, product_id__in=product):
            o.status_order = 2
            o.save()
        return Response('ok')


class TodayOrderCompleted(APIView):
    parser_classes = [FormParser, MultiPartParser]

    def get(self, request):
        Orders = Order.objects.filter(
            create_at__gte=datetime.datetime.now().date(), status_order=3)
        serializer = OrderSerializer(
            Orders, context={'request': request}, many=True)
        return Response(serializer.data)


class TodayOrderUnpaid(APIView):
    parser_classes = [FormParser, MultiPartParser]

    def get(self, request):
        Orders = Order.objects.filter(
            create_at__gte=datetime.datetime.now().date(), payment_status__in=[1, 2])
        serializer = OrderSerializer(
            Orders, context={'request': request}, many=True)
        return Response(serializer.data)


class TodayOrderOnGoing(APIView):
    parser_classes = [FormParser, MultiPartParser]

    def get(self, request):
        Orders = Order.objects.filter(
            create_at__gte=datetime.datetime.now().date(), status_order__in=[0, 1])
        serializer = OrderSerializer(
            Orders, context={'request': request}, many=True)
        return Response(serializer.data)


class TodayOrderVoid(APIView):
    parser_classes = [FormParser, MultiPartParser]

    def get(self, request):
        Orders = Order.objects.filter(
            create_at__gte=datetime.datetime.now().date(), status_order=4)
        serializer = OrderSerializer(
            Orders, context={'request': request}, many=True)
        return Response(serializer.data)


class OrderList(APIView):
    def get(self, request):
        Orders = Order.objects.all()
        serializer = OrderSerializer(Orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        # check customer
        if request.data['customer_set'] == {}:
            request.data['customer_id'] = None
            request.data['address_id'] = None
        elif not request.data['customer_id'] == None:
            if Customer.objects.filter(nick_name=request.data['customer_set']['nick_name'], phone_number=request.data['customer_set']['phone_number']).exists():
                request.data['customer_id'] = Customer.objects.get(
                    nick_name=request.data['customer_set']['nick_name'], phone_number=request.data['customer_set']['phone_number']).id
                if not request.data['address_set']['address'] == None:
                    if AddressCustomer.objects.filter(customer_id=request.data['customer_id'], address=request.data['address_set']['address']).exists():
                        request.data['address_id'] = AddressCustomer.objects.get(
                            customer_id=request.data['customer_id'], address=request.data['address_set']['address']).id
                else:
                    request.data['address_id'] = AddressCustomer.objects.create(
                        address=request.data['customer_set']['address_customer'], customer_id=request.data['customer_id'], status_address=3).id
            else:
                request.data['customer_id'] = Customer.objects.create(
                    phone_number=request.data['customer_set']['phone_number'], nick_name=request.data['customer_set']['nick_name']).id
                if not request.data['address_set']['address'] == None:
                    request.data['address_id'] = AddressCustomer.objects.create(
                        address=request.data['address_set']['address'], customer_id=request.data['customer_id'], status_address=3).id
        request.data['status_food'] = None
        request.data['status_drink'] = None

        product = [item['product_set']['type_product']
                   for item in request.data['orderitem_set'] if not 'topping' in item]
        topping = [item['topping_set']['type_topping']
                   for item in request.data['orderitem_set'] if 'topping' in item]
        for n in product:
            if n == 3 or n == 1:
                request.data['status_food'] = 0
            if n == 2:
                request.data['status_drink'] = 0

        for n in topping:
            if n == 3 or n == 1:
                request.data['status_food'] = 0
            if n == 2:
                request.data['status_drink'] = 0
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class OrderDetail(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise 404

    def get(self, request, pk):
        Order = self.get_object(pk)
        serializer = OrderSerializer(Order)
        return Response(serializer.data)

    def put(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        Order = self.get_object(pk)
        Order.delete()
        return Response(status=204)


class OrderItemList(APIView):
    def get(self, request):
        Orders = OrderItem.objects.all()
        serializer = OrderItemSerializer(Orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class OrderItemDetail(APIView):
    def get_object(self, pk):
        try:
            return OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist:
            raise 404

    def get(self, request, pk):
        Order = self.get_object(pk)
        serializer = OrderItemSerializer(Order)
        return Response(serializer.data)

    def put(self, request, pk):
        Order = self.get_object(pk)
        serializer = OrderItemSerializer(Order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        Order = self.get_object(pk)
        Order.delete()
        return Response(status=204)


class OrderItemToppingList(APIView):
    def get(self, request):
        Orders = OrderItemTopping.objects.all()
        serializer = OrderItemToppingSerializer(Orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderItemToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class OrderItemToppingDetail(APIView):
    def get_object(self, pk):
        try:
            return OrderItemTopping.objects.get(pk=pk)
        except OrderItemTopping.DoesNotExist:
            raise 404

    def get(self, request, pk):
        Order = self.get_object(pk)
        serializer = OrderItemToppingSerializer(Order)
        return Response(serializer.data)

    def put(self, request, pk):
        Order = self.get_object(pk)
        serializer = OrderItemToppingSerializer(Order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        Order = self.get_object(pk)
        Order.delete()
        return Response(status=204)


class AllOrder(APIView):
    def post(self, request):
        print(request.data)
        # order_before = request.data
        # order_before['']
        # order = OrderSerializer(data=request.data)
        # if order.is_valid():
        #     order.save()
        #     for product in request.data['cart']:
        #         product['order'] = order.data['id']
        #         product['product_id'] = product['product']['id']
        #         product_serializer = OrderItemSerializer(data=product)
        #         if product_serializer.is_valid():
        #             product_serializer.save()
        #             for topping in product['topping']:
        #                 topping['item'] = product_serializer.data['id']
        #                 topping['topping_id']  = topping['topping']['id']
        #                 topping_serializer = OrderItemToppingSerializer(data=topping)
        #                 if topping_serializer.is_valid:
        #                     topping_serializer.save()
        #                     return Response(order.data, status=201)
        #                 return Response(topping_serializer.errors,status=400)
        #         return Response(product_serializer.errors,status=400)
        # return Response(order.errors,status=400)
        return Response('ok')


class Report (APIView):
    def get(self, request):
        order = Order.objects.all()
        report = order.aggregate(Sum('total_balance'), Sum('discount'))
        report['total_order'] = order.count()
        report['total_cash'] = order.filter(
            payment_status=3).aggregate(Sum('total_balance'))['total_balance__sum']
        report['total_transfer'] = order.filter(
            payment_status=4).aggregate(Sum('total_balance'))['total_balance__sum']
        report['total_customer'] = order.filter(
            customer_id__isnull=False).values('customer_id').distinct().count()
        all_channel_id = [channel.id for channel in SaleChannel.objects.all()]
        # for channel_id in all_channel_id:

        report['sale_channel_detail'] = order.fitler
        # find top food
        filter_food = [
            product.id for product in Product.objects.filter(type_product=3)]
        all_food = OrderItem.objects.filter(product_id__in=filter_food,)
        top_food = all_food.annotate(frequency=Count('product_id')).order_by(
            'frequency').values('product_id').distinct()[:5]
        list_food = [t['product_id'] for t in top_food]
        top_product_data = Product.objects.filter(id__in=list_food)
        report['top_product'] = ProductReportSerialiser(
            top_product_data, many=True).data

        # find top drink
        filter_drink = [
            product.id for product in Product.objects.filter(type_product=2)]
        all_drink = OrderItem.objects.filter(product_id__in=filter_drink,)
        top_drink = all_drink.annotate(frequency=Count('product_id')).order_by(
            'frequency').values('product_id').distinct()[:5]
        list_drink = [t['product_id'] for t in top_drink]
        top_drink_data = Product.objects.filter(id__in=list_drink)
        report['top_drink'] = ProductReportSerialiser(
            top_drink_data, many=True).data

        # find top dressert
        filter_dressert = [
            product.id for product in Product.objects.filter(type_product=1)]
        all_dressert = OrderItem.objects.filter(
            product_id__in=filter_dressert,)
        top_dressert = all_dressert.annotate(frequency=Count('product_id')).order_by(
            'frequency').values('product_id').distinct()[:5]
        list_dressert = [t['product_id'] for t in top_dressert]
        top_dressert_data = Product.objects.filter(id__in=list_dressert)
        report['top_dressert'] = ProductReportSerialiser(
            top_dressert_data, many=True).data

        return Response(report, status=200)
