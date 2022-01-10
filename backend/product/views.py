import os
from django.db.models.fields.related import ManyToManyField

from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import (PriceProduct, Product,
                            ProductCategory, SaleChannel, Topping, ToppingCategory, SetTopping, PriceTopping)
from product.serializers import (PriceProductSerializer,
                                 PriceProductSerializer,
                                 ProductCategorySerializer, ProductSerializer,
                                 SaleChannelSerializer,
                                 ProductSerializer, ToppingSerializer, ToppingCategorySerializer, UpdateImageSaleS)

from .forms import *

# product category


class AmountPorduct(APIView):
    def get(self, request, category_id):
        product_amount = Product.objects.filter(
            category_id=category_id).count()
        return Response({'amount': product_amount}, status=200)


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


class ToppingByType(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, type):
        category = Topping.objects.filter(type_topping=type)
        serializer = ToppingSerializer(
            category, context={"request": request}, many=True)
        print(serializer.data)
        return Response(serializer.data, status=200)


class CategoryByType(APIView):
    def get(self, request, type):
        category = ProductCategory.objects.filter(type_category=type)
        serializer = ProductCategorySerializer(
            category, many=True)
        print(serializer.data)
        return Response(serializer.data, status=200)


class ProductByType(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, type):
        category = Product.objects.filter(type_product=type)
        serializer = ProductSerializer(
            category, context={"request": request}, many=True)
        print(serializer.data)
        return Response(serializer.data, status=200)


class ChangeList(APIView):
    def get(self, request):
        category = ProductCategory.objects.exclude(type_category=4)
        serializer = ProductCategorySerializer(
            category, context={"request": request}, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        if not ProductCategory.objects.filter(category=request.data['category']).exclude(type_category=4).exists():
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


class ToppingCategoryList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        category = ToppingCategory.objects.all()
        serializer = ToppingCategorySerializer(
            category, context={"request": request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not ToppingCategory.objects.filter(category=request.data['category']).exists():
            serializer = ToppingCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                print(request.data['select_topping'])
                for top_id in request.data['select_topping']:
                    if(not top_id == ','):
                        SetTopping.objects.create(
                            topping_id=top_id,
                            category_id=serializer.data['id']
                        )
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response('this caetgory name is already in use', status=400)


class AmountTopping(APIView):
    def get(self, request, category_id):
        product_amount = SetTopping.objects.filter(
            category_id=category_id).count()
        return Response({'amount': product_amount}, status=200)


class ToppingBySearch(APIView):

    def get(self, request, search):
        object = Topping.objects.filter(name__contains=search)
        serializer = ToppingSerializer(
            object, many=True)
        return Response(serializer.data)


class ToppingList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        object = Topping.objects.all()
        serializer = ToppingSerializer(
            object, context={"request": request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        if (not Product.objects.filter(code=request.data['code']).exists()) or (not Topping.objects.filter(code=request.data['code']).exists()):
            serializer = ToppingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                ezzone = SaleChannel.objects.get(sale_channel='EZZone').id
                PriceTopping.objects.create(
                    sale_channel_id=ezzone,
                    topping_id=serializer.data['id'],
                    price=request.data['price']
                )
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response('this code is already in use', status=400)


class ToppingCategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return ToppingCategory.objects.get(pk=pk)
        except ToppingCategory.DoesNotExist:
            raise 404

    def get(self, request, pk):
        sale_channel = ToppingCategory.objects.get(id=pk)
        serializer = ToppingCategorySerializer(
            sale_channel)
        return Response(serializer.data)

    def put(self, request, pk):
        sale_channel = self.get_object(pk)
        serializer = ToppingCategorySerializer(sale_channel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            SetTopping.objects.filter(category=serializer.data['id']).delete()
            for top_id in request.data['settopping_set']:
                if(not top_id == ','):
                    SetTopping.objects.create(
                        topping_id=top_id['topping'],
                        category_id=serializer.data['id']
                    )
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        sale_channel = ToppingCategory.objects.get(id=pk)
        sale_channel.delete()
        return Response(status=204)


class SaleChannelEzzone(APIView):
    def get(self, request):
        ezzone = SaleChannel.objects.get(sale_channel='EZZone')
        return Response({'id': ezzone.id}, status=200)


class SalechannelList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        sale_channel = SaleChannel.objects.all()
        serializer = SaleChannelSerializer(
            sale_channel, context={"request": request}, many=True)
        return Response(serializer.data)


class CreateSaleChannel(APIView):
    def post(self, request):
        serializer = SaleChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
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

    def get_object(self, pk):
        try:
            return SaleChannel.objects.get(pk=pk)
        except SaleChannel.DoesNotExist:
            raise 404

    def get(self, request, pk):
        sale_channel = self.get_object(pk)
        serializer = SaleChannelSerializer(sale_channel, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        sale_channel = self.get_object(pk)
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


class ProductByCategory(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, category_id):
        object = Product.objects.filter(category_id=category_id)
        serializer = ProductSerializer(
            object, context={"request": request}, many=True)
        return Response(serializer.data)


class CheckCategoryTopping(APIView):

    def get(self, request, category_name):
        object = ProductCategory.objects.filter(
            category=category_name, type_category=4).exists()
        return Response({'status': object})


class ProductList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        object = Product.objects.all()
        serializer = ProductSerializer(
            object, context={"request": request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        # if not Product.objects.filter(code=request.data['code']).exists():
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ezzone = SaleChannel.objects.get(sale_channel='EZZone').id
            PriceProduct.objects.create(
                sale_channel_id=ezzone,
                product_id=serializer.data['id'],
                price=request.data['price']
            )
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        # return Response('this code is already taked', status=400)


class ProductStatus(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise 404

    def put(self, request, pk):
        topping = self.get_object(pk)
        topping.status = request.data['status']
        topping.update_by_id = request.data['update_by']
        topping.save()
        serializer = ProductSerializer(topping)
        return Response(serializer.data)


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
        print(object)
        # if (len(request.FILES) != 0) and (object.img != None):
        #     os.remove(object.img.path)
        #     object.img = request.FILES['img']
        serializer = ProductSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        os.remove(object.img.path)
        object.delete()
        return Response(status=204)


class ProductPos(APIView):
    def get(self, request):
        topping = Product.objects.filter(status=True)
        serializer = ProductSerializer(topping, many=True)
        return Response(serializer.data)


# price product
class UpdateImageSaleChannel(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, pk):
        sale_channel = SaleChannel.objects.get(pk=pk)
        serializer = UpdateImageSaleS(
            sale_channel, context={"request": request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        sale_channel = SaleChannel.objects.get(pk=pk)
        serializer = UpdateImageSaleS(sale_channel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


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
                    price = PriceProduct.objects.get(pk=item['id'])
                    serializer = PriceProductSerializer(price, data=item)
                    if serializer.is_valid():
                        price.save()
                        return Response('ok', status=200)
                    return Response('bad request', status=400)


class ProductByTypeAndSearch(APIView):
    def get(self, request, type, search):
        product = Product.objects.filter(
            name__contains=search, type_product=type)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=200)


class DeleteSaleChannel(APIView):
    def put(self, request):
        SaleChannel.objects.filter(pk__in=request.data['list']).delete()
        sale_chanenl = SaleChannel.objects.all()
        serializer = SaleChannelSerializer(sale_chanenl,many=True)
        return Response(serializer.data,status=200)
