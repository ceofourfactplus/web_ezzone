from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import RawMaterial, RawMaterialCategory, Unit
from .serializers import RawMaterialCategorySerializer, UnitSerializer, RawMaterialSerializer
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
            if request.data['to_unit_id'] != '':
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
    def get(self, request, pk):
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


class FilCategoryRaw(APIView):
    def get(self, request, pk):
        raw_material = RawMaterial.objects.filter(category_id=pk)
        serializer = RawMaterialSerializer(raw_material, many=True)
        return Response(serializer.data)


class PONotice(APIView):
    def get(self, request):
        raw_material = RawMaterial.objects.filter(status__gt=1)
        serializer = RawMaterialSerializer(raw_material, many=True)
        return Response(serializer.data)


class GetSupplier(APIView):
   def get(self,request,raw_id):
       get_max_unit(raw_id)
       return Response('ok')