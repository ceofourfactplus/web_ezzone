from rest_framework import serializers
from .models import RawMaterialCategory, RawMaterial, ReceiptRawMaterial, ReceiptRawMaterial, Supplier, Unit, PickUpRawMaterial, ReceiptRawMaterialDetail
from user.serializers import UserSerializer


class RawMaterialListSeriallizer(serializers.ModelSerializer):
    
    class Meta:
        model = RawMaterial
        fields = '__all__'

class RawMaterialCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterialCategory
        fields = ['id', 'name']


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class RawMaterialSerializer(serializers.ModelSerializer):
    unit_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    create_by_id = serializers.IntegerField()
    update_by_id = serializers.IntegerField()
    max_price_supplier_id = serializers.IntegerField()
    min_price_supplier_id = serializers.IntegerField()
    create_by_set = UserSerializer(read_only=True, source="user")
    update_by_set = UserSerializer(read_only=True, source="user")
    category_set = RawMaterialCategorySerializer(
        read_only=True, source="raw_material_category")
    min_price_supplier_set = SupplierSerializer(read_only=True, source="supplier")
    max_price_supplier_set = SupplierSerializer(read_only=True, source="supplier")
    unit_set = UnitSerializer(read_only=True, source="unit")

    class Meta:
        model = RawMaterial
        fields = [
            'id',
            'img',
            'status',
            'name',
            'balance',
            'minimum',
            'avg_price',
            'max_price',
            'min_price',
            'max_price_supplier_id',
            'min_price_supplier_id',
            'in_refrigerator',
            'create_by_id',
            'update_by_id',
            'category_id',
            'unit_id',
            'create_at',
            'update_at',
            'category_set',
            'max_price_supplier_set',
            'min_price_supplier_set',
            'update_by_set',
            'create_by_set',
            'unit_set',
        ]


class PickUpRawMaterialSerializer(serializers.ModelSerializer):
    raw_material_set = RawMaterialSerializer(
        read_only=True, source="raw_material")
    raw_material_id = serializers.IntegerField()
    create_by_id = serializers.IntegerField()
    create_by = UserSerializer(read_only=True, source="user")

    class Meta:
        model = PickUpRawMaterial
        fields = ['id', 'raw_material_set', 'raw_material_id',
                  'amount', 'create_at', 'create_by', 'create_by_id']


class ReceiptRawMaterialDetailSerializer(serializers.ModelSerializer):
    invoice_id = serializers.IntegerField()
    raw_material_id = serializers.IntegerField()
    raw_material_set = RawMaterialSerializer(
        read_only=True, source="raw_material")
    supplier_id = serializers.IntegerField()
    supplier_set = SupplierSerializer(read_only=True, source="supplier")
    create_by_id = serializers.IntegerField()
    update_by_id = serializers.IntegerField()
    create_by = UserSerializer(read_only=True, source="user")
    update_by = UserSerializer(read_only=True, source="user")

    class Meta:
        model = ReceiptRawMaterialDetail
        fields = ['id', 'invoice_id', 'raw_material_id', 'price',
                  'total_price', 'amount', 'remark', 'discount',
                  'create_at', 'create_by_id', 'update_at',
                  'update_by_id', 'supplier_id', 'supplier_set',
                  'invoice_set', 'raw_material_set', 'create_by',
                  'update_by']


class ReceiptRawMaterialSerializer(serializers.ModelSerializer):
    supplier_set = SupplierSerializer(read_only=True, source="supplier")
    supplier_id = serializers.IntegerField()
    receipt_raw_material_detail_list = ReceiptRawMaterialDetailSerializer(
        read_only=True, many=True, source="receipt_raw_material_detail")
    create_by_id = serializers.IntegerField()
    update_by_id = serializers.IntegerField()
    create_by = UserSerializer(read_only=True, source="user")
    update_by = UserSerializer(read_only=True, source="user")

    class Meta:
        model = ReceiptRawMaterial
        fields = ['id', 'supplier_id', 'total_price',
                  'total_amount', 'payment', 'receipt_raw_material_detail_list'
                  'create_at', 'create_by_id', 'update_by_id',
                  'update_at', 'supplier_set',
                  'create_by', 'update_by']
