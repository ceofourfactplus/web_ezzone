from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import RawMaterial, RawMaterialCategory, Unit,Supplier
from .serializers import RawMaterialCategorySerializer, UnitSerializer, RawMaterialSerializer,SupplierSerializer
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

    def put(self, request, pk, pa):
        raw_material = self.get_object(pk)
        raw_material.remain -= pa
        raw_material.save()
        serializer = RawMaterialSerializer(raw_material)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = RawMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('serializer', serializer.data['id'])
            print('request', request.data)
            return Response(serializer.data, status=201)
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


class PONotice(APIView):
    def get(self, request):
        raw_material = RawMaterial.objects.filter(remain__lte = F('minimum'))
        serializer = RawMaterialSerializer(raw_material, many=True)
        return Response(serializer.data)

    def post(self,request):
        return Response('ok')

