from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import RawMaterial, RawMaterialCategory, Unit, Supplier, PickUpRawMaterial, PO
from .serializers import RawMaterialCategorySerializer, UnitSerializer, RawMaterialSerializer, SupplierSerializer, PickUpRawMaterialSerializer, POSerializer

from django.db.models import F
from rest_framework.parsers import FormParser, MultiPartParser





class RawMaterialListAPIView(APIView):
    def get_object(self, pk):
        try:
            return RawMaterial.objects.get(pk=pk)
        except RawMaterial.DoesNotExist:
            raise 404

    def get(self, request):
        RawMaterials = RawMaterial.objects.all()
        serializer = RawMaterialSerializer(RawMaterials, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        pickup_serializer = PickUpRawMaterialSerializer(data=request.data)
        if pickup_serializer.is_valid():
            pickup_serializer.save()
            raw_material = self.get_object(request.data['raw_material_id'])
            raw_material.remain -= int(request.data['amount'])
            if raw_material.remain <= raw_material.minimum and raw_material.remain > 0:
                raw_material.status = 2
            elif raw_material.remain <= 0:
                raw_material.status = 3
            raw_material.save()
            serializer = RawMaterialSerializer(raw_material)
            return Response(serializer.data, status=200)
        return Response(pickup_serializer.errors, status=400)
    
    def post(self, request):
        print(request.data, 'data')
        serializer = RawMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('serializer', serializer.data['id'])
            print('request', request.data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PickupAPIView(APIView):
    def get(self, request):
        pickup = PickUpRawMaterial.objects.all()
        serializer = PickUpRawMaterialSerializer(pickup, many=True)
        return Response(serializer.data)
    
    
class RMAPIView(APIView):
    def get_object(self, pk):
        try:
            return RawMaterial.objects.get(pk=pk)
        except RawMaterial.DoesNotExist:
            raise 404
    
    def get(self, request, pk):
        raw_material = self.get_object(pk)
        serializer = RawMaterialSerializer(raw_material)
        return Response(serializer.data)
    
    def put(self, request):
        print(request.data)
        raw_material = self.get_object(int(request.data['raw_material_id'][0]))
        serializer = RawMaterialSerializer(raw_material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class SupplierListAPIView(APIView):
    def get(self, request):
        Suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(Suppliers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SupplierDetailAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def get_object(self, pk):
        try:
            return Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            raise 404

    def get(self, request, pk):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        supplier = self.get_object(pk)
        supplier.delete()
        return Response(status=204)


class UnitListAPIView(APIView):

    def get(self, request):
        unit = Unit.objects.all()
        serializer = UnitSerializer(unit, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UnitDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Unit.objects.get(pk=pk)
        except Unit.DoesNotExist:
            raise 404

    def get(self, request, pk):
        unit = self.get_object(pk)
        serializer = UnitSerializer(unit)
        return Response(serializer.data)

    def put(self, request, pk):
        unit = self.get_object(pk)
        serializer = UnitSerializer(unit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        unit = self.get_object(pk)
        unit.delete()
        return Response(status=204)


class CategoryAPIView(APIView):
    def get(self, request):
        category = RawMaterialCategory.objects.all()
        serializer = RawMaterialCategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not RawMaterialCategory.objects.filter(name=request.data['name']).exists():
            serializer = RawMaterialCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response('this caetgory name is already in use', status=400)


class RMCategoryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return RawMaterialCategory.objects.get(pk=pk)
        except RawMaterialCategory.DoesNotExist:
            raise 404

    def get(self, request, pk):
        category = RawMaterialCategory.objects.get(id=pk)
        serializer = RawMaterialCategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        unit = self.get_object(pk)
        serializer = RawMaterialCategorySerializer(unit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class CategoryFilter(APIView):
    def get(self, request, q):
        if Category.objects.filter(name__contains=q).exists:
            category = Category.objects.filter(name__contains=q)
        else:
            category = Category.objects.all()[:5]
        serializer = CategorySerializer(category, many=True)
        print(serializer.data)
        return Response(serializer.data)


class FilCategoryRaw(APIView):
    def get(self, request, pk):
        raw_material = RawMaterial.objects.filter(category_id=pk)
        serializer = RawMaterialSerializer(raw_material, many=True)
        return Response(serializer.data)
    
class PO(APIView):
    def get(self, request):
        po = PO.objects.all()
        serializer = POSerializer(po, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = POSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PONotice(APIView):
    def get(self, request):
        RawMaterials = RawMaterial.objects.filter(minimum__gt = F('remain'))
        print(RawMaterials)
        for item in RawMaterials:
            if item.remain <= item.minimum and item.remain > 0:
                item.status = 2
            elif item.remain <= 0:
                item.status = 3
            item.save()
        serializer = RawMaterialSerializer(RawMaterials, many=True)
        return Response(serializer.data)

    def post(self,request):
        return Response('ok')

