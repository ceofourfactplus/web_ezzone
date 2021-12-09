import os

from django.contrib import messages
from django.db.models.query_utils import RegisterLookupMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from product.models import (PriceProduct, PriceTopping, Product,
                            ProductCategory, SaleChannel, TableTopping,
                            Topping, TypeTopping)
from product.serializers import (PriceProductSerializer,
                                 PriceToppingSerializer,
                                 ProductCategorySerializer, ProductSerializer,
                                 SaleChannelSerializer, TableToppingSerializer,
                                 ToppingSerializer, TypeToppingSerializer)

from .forms import *

# product category

class ProductCategoryStatus(APIView):
    def get_object(self, pk):
        try:
            return ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            raise 404

    def put(self, request, pk):
        sale_channel = self.get_object(pk)
        sale_channel.status = request.data['status']
        sale_channel.update_by_id = request.data['update_by']
        sale_channel.save()
        serializer = ProductCategorySerializer(sale_channel)
        return Response(serializer.data)


class ProductCategoryList(APIView):
    def get(self, request):
        category = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(
            category, context={"request": request}, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        if not ProductCategory.objects.filter(category=request.data['category']).exists():
            serializer = ProductCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response('this caetgory name is already in use', status=400)


class ProductCategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            return Response('not found data', status=400)

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = ProductCategorySerializer(
            category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = ProductCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=204)

# sale channel


class SalechannelList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        sale_channel = SaleChannel.objects.all()
        serializer = SaleChannelSerializer(
            sale_channel, context={"request": request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SaleChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SaleChannelStatus(APIView):
    def get_object(self, pk):
        try:
            return SaleChannel.objects.get(pk=pk)
        except SaleChannel.DoesNotExist:
            raise 404

    def put(self, request, pk):
        sale_channel = self.get_object(pk)
        sale_channel.status = request.data['status']
        sale_channel.update_by_id = request.data['update_by']
        sale_channel.save()
        serializer = SaleChannelSerializer(sale_channel)
        return Response(serializer.data)


class SaleChannelDetail(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return SaleChannel.objects.get(pk=pk)
        except SaleChannel.DoesNotExist:
            raise 404

    def get(self, request, pk):
        sale_channel = self.get_object(pk)
        serializer = SaleChannelSerializer(
            sale_channel, context={"request": request}, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        sale_channel = self.get_object(pk)
        if len(request.FILES) != 0:
            os.remove(sale_channel.img.path)
            sale_channel.img = request.FILES['img']
        serializer = SaleChannelSerializer(sale_channel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        sale_channel = self.get_object(pk)
        os.remove(sale_channel.img.path)
        sale_channel.delete()
        return Response(status=204)

# topping


class ToppingList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        object = Topping.objects.all()
        serializer = ToppingSerializer(
            object, context={"request": request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not Topping.objects.filter(code=request.data['code']).exists():
            serializer = ToppingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response('this code is already taked', status=400)


class ToppingStatus(APIView):
    def get_object(self, pk):
        try:
            return Topping.objects.get(pk=pk)
        except Topping.DoesNotExist:
            raise 404

    def put(self, request, pk):
        topping = self.get_object(pk)
        topping.status = request.data['status']
        topping.update_by_id = request.data['update_by']
        topping.save()
        serializer = ToppingSerializer(topping)
        return Response(serializer.data)


class ToppingDetail(APIView):
    def get_object(self, pk):
        try:
            return Topping.objects.get(pk=pk)
        except Topping.DoesNotExist:
            raise 404

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = ToppingSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object(pk)
        if len(request.FILES) != 0:
            os.remove(object.img.path)
            object.img = request.FILES['img']
        serializer = ToppingSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        os.remove(object.img.path)
        object.delete()
        return Response(status=204)


class ToppingPos(APIView):
    def get(self, request):
        topping = Topping.objects.filter(status=True)
        serializer = ToppingSerializer(topping, many=True)
        return Response(serializer.data)




# type topping

class TypeToppingList(APIView):
    def get(self, request):
        object = TypeTopping.objects.all()
        serializer = TypeToppingSerializer(object, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TypeToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TypeToppingDetail(APIView):
    def get_object(self, pk):
        try:
            return TypeTopping.objects.get(pk=pk)
        except TypeTopping.DoesNotExist:
            raise 404

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = TypeToppingSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object(pk)
        serializer = TypeToppingSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        return Response(status=204)

# price topping


class PriceToppingList(APIView):
    def get(self, request):
        object = PriceTopping.objects.all()
        serializer = PriceToppingSerializer(object, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PriceToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PriceToppingDetail(APIView):
    def get_object(self, pk):
        try:
            return PriceTopping.objects.get(pk=pk)
        except PriceTopping.DoesNotExist:
            raise 404

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = PriceToppingSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object(pk)
        serializer = PriceToppingSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        return Response(status=204)

class PriceToppingMany(APIView):
    def post(self, request):
        for data in request.data:
            PriceTopping.objects.create(
                topping_id=data['id'],
                sale_channel_id=data['sale_channel_id'],
                price=data['new_price'],
                create_by_id=data['create_by'],
                update_by_id=data['update_by']
            )
        return Response('ok')

    def put(self, request):
        for data in request.data:
            for item in data['price_topping']:
                if item['sale_channel_id']==data['sale_channel_edit']:
                    price = PriceTopping.objects.get(id = item['id'])
                    serializer = PriceToppingSerializer(price,data=item)
                    if serializer.is_valid(): 
                        price.save()
                        return Response('ok')
                    return Response(serializer.errors,status=400)
                
# table topping


class TableToppingList(APIView):
    def get(self, request):
        object = TableTopping.objects.all()
        serializer = TableToppingSerializer(object, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TableToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TableToppingDetail(APIView):
    def get_object(self, pk):
        try:
            return TableTopping.objects.get(pk=pk)
        except TableTopping.DoesNotExist:
            raise 404

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = TableToppingSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object(pk)
        serializer = TableToppingSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        return Response(status=204)

# price product


class PriceProductList(APIView):
    def get(self, request):
        object = PriceProduct.objects.all()
        serializer = PriceProductSerializer(object, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PriceProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PriceProductDetail(APIView):
    def get_object(self, pk):
        try:
            return PriceProduct.objects.get(pk=pk)
        except PriceProduct.DoesNotExist:
            raise 404

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = PriceProductSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object(pk)
        serializer = PriceProductSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        return Response(status=204)


class PriceProductMany(APIView):
    def post(self, request):
        for data in request.data:
            PriceProduct.objects.create(
                product_id=data['id'],
                sale_channel_id=data['sale_channel_id'],
                price=data['new_price'],
                create_by_id=data['create_by'],
                update_by_id=data['update_by']
            )
        return Response('ok')

    def put(self, request):
        for data in request.data:
            for item in data['price']:
                if item['sale_channel_id'] == data['sale_channel_edit']:
                    price = PriceProduct.objects.get(pk = item['id'])
                    serializer = PriceProductSerializer(price,data=item)
                    if serializer.is_valid():
                        price.save()
                        return Response('ok',status=200)
                    return Response('bad request',status=400)
                

# product

class ProductList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        object = Product.objects.all()
        serializers = ProductSerializer(
            object, context={"request": request}, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        print(request.data['code'])
        if not Product.objects.filter(code=request.data['code']).exists():
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response('this code is already taked', status=400)


class ProductDetail(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise 404

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = ProductSerializer(object, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object(pk)
        if len(request.FILES) != 0:
            os.remove(object.img.path)
            object.img = request.FILES['img']
        serializer = ProductSerializer(
            object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        os.remove(object.img.path)
        object.delete()
        return Response('delete success!', status=204)


class ProductStatus(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise 404

    def put(self, request, pk):
        product = self.get_object(pk)
        product.status = request.data['status']
        product.update_by_id = request.data['update_by']
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductPos(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request,pk):
        product = Product.objects.filter(status=True,category_id=pk)
        serializer = ProductSerializer(
            product, many=True, context={"request": request})
        return Response(serializer.data)
