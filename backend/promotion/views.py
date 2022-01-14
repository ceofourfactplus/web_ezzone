from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import PointPromotion, Rewards, ConditionRewards, Voucher, Redemption, PromotionPackage, PackageItem, ItemTopping, CustomerPoint
from .serializers import PointSerializer, VoucherSerializer, PromotionPackageSerializer, PackageItemSerializer, ItemToppingSerializer


class PointPromotionAPI(APIView):
    def get_object(self, pk):
        try:
            return PointPromotion.objects.get(id=pk)
        except PointPromotion.DoesNotExist:
            raise 404
        
    def get(self, request):
        point = PointPromotion.objects.all()
        serializer = PointSerializer(point, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        point = self.get_object(request.data['id'])
        serializer = PointSerializer(point, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def post(self, request):
        serializer = PointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class Point(APIView):
    def get_object(self, pk):
        try:
            return PointPromotion.objects.get(id=pk)
        except PointPromotion.DoesNotExist:
            raise 404
        
    def get(self, request, pk):
        point = self.get_object(pk)
        serializer = PointSerializer(point)
        return Response(serializer.data)
        
class VoucherAPI(APIView):
    def get_object(self, pk):
        try:
            return Voucher.objects.get(id=pk)
        except Voucher.DoesNotExist:
            raise 404
        
    def get(self, request):
        voucher = Voucher.objects.all()
        serializer = VoucherSerializer(voucher, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        voucher = Voucher.objects.get(id=request.data['id'])
        serializer = VoucherSerializer(voucher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def post(self, request):
        serializer = VoucherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class VoucherGET(APIView):
    def get_object(self, pk):
        try:
            return Voucher.objects.get(id=pk)
        except Voucher.DoesNotExist:
            raise 404
        
    def get(self, request, pk):
        voucher = self.get_object(pk)
        serializer = VoucherSerializer(voucher)
        return Response(serializer.data)
    
class PackageAPI(APIView):
    def get_object(self, pk):
        try:
            return PromotionPackage.objects.get(id=pk)
        except PromotionPackage.DoesNotExist:
            raise 404
        
    def get(self, request):
        package = PromotionPackage.objects.all()
        serializer = PromotionPackageSerializer(package, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        package = PromotionPackage.objects.get(id=request.data['id'])
        serializer = PromotionPackageSerializer(package, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def post(self, request):
        serializer = PromotionPackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class PackageGET(APIView):
    def get_object(self, pk):
        try:
            return PromotionPackage.objects.get(id=pk)
        except PromotionPackage.DoesNotExist:
            raise 404
        
    def get(self, request, pk):
        package = self.get_object(pk)
        serializer = PromotionPackageSerializer(package)
        return Response(serializer.data)
    
class PackageItemAPI(APIView):
    def get_object(self, pk):
        try:
            return PackageItem.objects.get(id=pk)
        except PackageItem.DoesNotExist:
            raise 404
        
    def get(self, request):
        package = PackageItem.objects.all()
        serializer = PackageItemSerializer(package, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        package = PackageItem.objects.get(id=request.data['id'])
        serializer = PackageItemSerializer(package, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def post(self, request):
        serializer = PackageItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class ItemToppingToppingAPI(APIView):
    def get_object(self, pk):
        try:
            return ItemTopping.objects.get(id=pk)
        except ItemTopping.DoesNotExist:
            raise 404
        
    def get(self, request):
        item_topping = ItemTopping.objects.all()
        serializer = ItemToppingSerializer(item_topping, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        item_topping = ItemTopping.objects.get(id=request.data['id'])
        serializer = ItemToppingSerializer(item_topping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def post(self, request):
        serializer = ItemToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)