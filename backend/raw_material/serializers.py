from rest_framework import serializers
from .models import RawMaterialCategory, RawMaterial, ReceiptRawMaterial, ReceiptRawMaterial, Supplier, Unit, PickUpRawMaterial, ReceiptRawMaterialDetail
from user.serializers import UserSerializer


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
    unit_set = UnitSerializer(read_only=True, source="unit")
    category_id = serializers.IntegerField()
    category_set = RawMaterialCategorySerializer(
        read_only=True, source="raw_material_category")
    create_by_id = serializers.IntegerField()
    update_by_id = serializers.IntegerField()
    create_by = UserSerializer(read_only=True, source="user")
    update_by = UserSerializer(read_only=True, source="user")

    class Meta:
        model = RawMaterial
        fields = ['id', 'code', 'status', 'name', 'balance', 'unit_id', 'minraw_material',
                  'avg_price', 'max_price', 'min_price', 'create_by', 'update_by', 'create_by_id', 
                  'update_by_id','create_at', 'update_at', 'unit_set', 'category_id', 'category_set']


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
                  'total_amount', 'payment','receipt_raw_material_detail_list'
                  'create_at', 'create_by_id', 'update_by_id',
                  'update_at', 'supplier_set',
                  'create_by', 'update_by']
