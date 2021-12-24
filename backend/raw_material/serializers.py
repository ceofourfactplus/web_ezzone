from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import  RawMaterialCategory, RawMaterial, ReceiptRawMaterial, ReceiptRawMaterial, Supplier, Unit, PickUpRawMaterial, ReceiptRawMaterialDetail, PO
from user.serializers import UserSerializer


class RawMaterialListSeriallizer(serializers.ModelSerializer):
    
    class Meta:
        model = RawMaterial
        fields = '__all__'

class RawMaterialCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterialCategory
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
        
        
class POSerializer(serializers.ModelSerializer):
    raw_material_id = serializers.IntegerField(required=True)
    supplier_id = serializers.IntegerField(required=True)
    create_by_id = serializers.IntegerField(required=True)
    unit_id = serializers.IntegerField(required=True)
    supplier_set = SupplierSerializer(read_only=True, source="supplier")
    raw_material_set = RawMaterialListSeriallizer(
        read_only=True, source="raw_material")
    class Meta:
        model = PO
        fields = [
            'amount',
            'status',
            'unit_id',
            'supplier_set',
            'raw_material_set',
            'raw_material_id',
            'supplier_id',
            'create_by_id',
            'create_at',
        ]

class RawMaterialSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(required=True)
    create_by_id = serializers.IntegerField(required=True)
    update_by_id = serializers.IntegerField()
    create_by_set = UserSerializer(read_only=True, source="user")
    update_by_set = UserSerializer(read_only=True, source="user")
    category_set = RawMaterialCategorySerializer(
        read_only=True, source="raw_material_category")
    unit_set = UnitSerializer(read_only=True, source="unit")
    unit_l_id = serializers.IntegerField()
    unit_m_id = serializers.IntegerField()
    unit_s_id = serializers.IntegerField()

    class Meta:
        model = RawMaterial
        fields = [
            'id',
            'img',
            'status',
            'name',
            'minimum',
            'remain',
            'maximum',  
            'in_refrigerator',
            'create_by_id',
            'update_by_id',
            'category_id',
            'unit_l_id',
            'unit_m_id',
            'unit_s_id',
            'm_to_l',
            's_to_m',
            'avg_l',
            'avg_m',
            'avg_s',
            'create_at',
            'update_at',
            'category_set',
            'update_by_set',
            'create_by_set',
            'unit_set',
        ]


class PickUpRawMaterialSerializer(serializers.ModelSerializer):
    unit_set = UnitSerializer(read_only=True, source="unit")
    raw_material_set = RawMaterialSerializer(
        read_only=True, source="raw_material")
    raw_material_id = serializers.IntegerField()
    unit_id = serializers.IntegerField()
    create_by_id = serializers.IntegerField()
    create_by = UserSerializer(read_only=True, source="user")
    class Meta:
        model = PickUpRawMaterial
        fields = [
            'id', 
            'raw_material_set', 
            'unit_id',
            'unit_set', 
            'raw_material_id',
            'amount', 
            'create_at', 
            'create_by', 
            'create_by_id',
            ]


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
