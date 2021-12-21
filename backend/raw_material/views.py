from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import RawMaterialCategory
from .serializers import RawMaterialCategorySerializer
# Create your views here.


class RawMaterialListAPIView(APIView):
    def get(self, request):
        RawMaterials = RawMaterial.objects.all()
        serializer = RawMaterialListSeriallizer(RawMaterials, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RawMaterialListSeriallizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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


class StockListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)

    def post(self, request):
        if Category.objects.filter(name=request.data['category']).exists():
            category_id = Category.objects.get(
                name=request.data['category']).id
        else:
            new_category = Category.objects.create(
                name=request.data['category']
            )
            print(new_category.id)
            category_id = new_category.id
        if Unit.objects.filter(unit=request.data['unit']).exists():
            unit_id = Unit.objects.get(unit=request.data['unit']).id
        else:
            new_unit = Unit.objects.create(unit=request.data['unit'])
            print(new_unit)
            unit_id = new_unit.id

        if Stock.objects.filter(code=request.data['code']).exists():
            return Response('has been taked ', status=400)
        request.data['unit_id'] = unit_id
        request.data['category_id'] = category_id
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class StockDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise 404

    def get(self, request, pk):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def put(self, request, pk):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        stock = self.get_object(pk)
        stock.delete()
        return Response(status=204)


class InvoiceListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        invoice = Invoice.objects.all()
        serializer = InvoiceSerializer(invoice, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class InvoiceDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            raise 404

    def get(self, request, pk):
        invoice = self.get_object(pk)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

    def put(self, request, pk):
        invoice = self.get_object(pk)
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        invoice = self.get_object(pk)
        invoice.delete()
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


class PayerListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        payer = Payer.objects.all()
        serializer = PayerSerializer(payer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PayerDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Payer.objects.get(pk=pk)
        except Payer.DoesNotExist:
            raise 404

    def get(self, request, pk):
        payer = self.get_object(pk)
        serializer = PayerSerializer(payer)
        return Response(serializer.data)

    def put(self, request, pk):
        payer = self.get_object(pk)
        serializer = PayerSerializer(payer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        payer = self.get_object(pk)
        payer.delete()
        return Response(status=204)


class StockTranceListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        stocktrance = StockTrance.objects.all()
        serializer = StockTranceSerializer(stocktrance, many=True)
        return Response(serializer.data)

    def post(self, request):
        stock = Stock.objects.get(id=request.data["stock_id"])
        stock.balance = stock.balance-request.data["amount"]
        stock.save()
        serializer = StockTranceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class StockTranceDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return StockTrance.objects.get(pk=pk)
        except StockTrance.DoesNotExist:
            raise 404

    def get(self, request, pk):
        stock_trance = self.get_object(pk)
        serializer = StockTranceSerializer(stock_trance)
        return Response(serializer.data)

    def put(self, request, pk):
        stock_trance = self.get_object(pk)
        serializer = StockTranceSerializer(stock_trance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        stock_trance = self.get_object(pk)
        stock_trance.delete()
        return Response(status=204)

class InvoiceDetailListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        invoice_detail = InvoiceDetail.objects.all()
        serializer = InvoiceDetailSerializer(invoice_detail, many=True)
        return Response(serializer.data)

    def post(self, request):
        invoicedetail = request.data
        stock = Stock.objects.get(id=request.data["stock_id"])
        stock.balance = stock.balance+invoicedetail["amount"]
        if(stock.min_price > invoicedetail["price"]):
            stock.min_price = invoicedetail["price"]
        if(stock.max_price < invoicedetail["price"]):
            stock.max_price = invoicedetail["price"]
        stock.save()
        # Stock(balance = (serializer["balance"] + invoice_stock),minstock=1).save()

        serializer = InvoiceDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class InvoiceDetailDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return InvoiceDetail.objects.get(pk=pk)
        except InvoiceDetail.DoesNotExist:
            raise 404

    def get(self, request, pk):
        invoice_detail = self.get_object(pk)
        serializer = InvoiceDetailSerializer(invoice_detail)
        return Response(serializer.data)

    def put(self, request, pk):
        invoice_detail = self.get_object(pk)
        serializer = InvoiceDetailSerializer(invoice_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        invoice_detail = self.get_object(pk)
        invoice_detail.delete()
        return Response(status=204)


class DeleteAllDataAPIView(APIView):
    def get(self, request):
        Stock.objects.all().delete()
        StockTrance.objects.all().delete()
        Unit.objects.all().delete()
        Supplier.objects.all().delete()
        Payer.objects.all().delete()
        Invoice.objects.all().delete()
        InvoiceDetail.objects.all().delete()
        return Response('ok')


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


class CategoryDetailAPIView(APIView):
    def get(self, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
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


class UnitFil(APIView):
    def get(self, request, q):
        if Unit.objects.filter(unit__contains=q).exists:
            unit = Unit.objects.filter(unit__contains=q)
        else:
            unit = Unit.objects.all()

        serializer = UnitSerializer(unit, many=True)
        return Response(serializer.data)


class StockFrequency(APIView):
    def get(self, request, stock_id):
            stocktrance = StockTrance.objects.filter(
            create_at__month__gte=1, stock_id=stock_id)
            serializer = StockTranceSerializer(stocktrance, many=True)
            return Response(serializer.data)

from django.db.models import F
class ToBuyStock(APIView):
    def get(self, request):
        all_stock = Stock.objects.filter(balance__lte=F('minstock'))
        serializer = StockSerializer(all_stock,many=True)
        return Response(serializer.data)