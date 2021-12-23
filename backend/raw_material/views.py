from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import PriceUnit, MultiUnit, RawMaterial, RawMaterialCategory, Unit
from .serializers import RawMaterialCategorySerializer, UnitSerializer, RawMaterialSerializer, PickUpRawMaterialSerializer
# Create your views here.


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
            if raw_material.remain <= raw_material.minimum and raw_material.remain != 0:
                raw_material.status = 2
            elif raw_material.remain == 0:
                raw_material.status = 3
            raw_material.save()
            serializer = RawMaterialSerializer(raw_material)
            return Response(serializer.data, status=200)
        return Response(pickup_serializer.errors, status=400)
    

    def post(self, request):
        serializer = RawMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('serializer', serializer.data['id'])
            print('request', request.data)
            if request.data['to_unit_id'] != None:
                MultiUnit.objects.create(
                    raw_material_id=serializer.data['id'],
                    unit_id=serializer.data['unit_id'],
                    to_unit_id=request.data['to_unit_id'],
                    to_amount=request.data['to_amount']
                )
                PriceUnit.objects.create(avg_price=0, max_price=0, min_price=0,
                                         raw_material_id=serializer.data['id'], unit_id=serializer.data['unit_id'])
                # if request.data['next_unit_id'] != None:
                #     MultiUnit.objects.create(
                #         raw_material_id=serializer.data['id'],
                #         unit_id=request.data['to_unit_id'],
                #         to_unit_id=request.data['next_unit_id'],
                #         to_amount=request.data['next_amount']
                #     )
                #     PriceUnit.objects.create(avg_price=0, max_price=0, min_price=0,
                #                              raw_material_id=serializer.data['id'], unit_id=serializer.data['unit_id'])
                #     return Response(serializer.data, status=201)
                return Response(serializer.data, status=201)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


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
        raw_material = self.get_object(int(request.data['raw_material_id'][0]))
        serializer = RawMaterialSerializer(raw_material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class SupplierListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

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
    def get_object(self, pk):
        try:
            return Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            raise 404

    def get(self, request, pk):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier)
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
    def get(self,request, pk):
        category = RawMaterialCategory.objects.get(id=pk)
        serializer = RawMaterialCategorySerializer(category)
        return Response(serializer.data)


class CategoryFilter(APIView):
    def get(self, request, q):
        if Category.objects.filter(name__contains=q).exists:
            category = Category.objects.filter(name__contains=q)
        else:
            category = Category.objects.all()[:5]
        serializer = CategorySerializer(category, many=True)
        print(serializer.data)
        return Response(serializer.data)
