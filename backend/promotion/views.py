from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import ast
from .models import PointPromotion, Rewards, ConditionRewards, Voucher, Redemption, PromotionPackage, PackageItem, ItemTopping, CustomerPoint, ExchangeHistory
from .serializers import PointSerializer, VoucherSerializer, PromotionPackageSerializer, PackageItemSerializer, ItemToppingSerializer, RewardsSerializer, ConditionRewardsSerializer, CustomerPointSerializer


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
    
    def put(self, request, pk):
        point = self.get_object(pk)
        point.status = request.data['status']
        point.save()
        serializer = PointSerializer(point)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        point = self.get_object(pk)
        point.delete()
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
    
    def put(self, request, pk):
        voucher = self.get_object(pk)
        voucher.status = request.data['status']
        voucher.save()
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
    
    def put(self, request, pk):
        package = self.get_object(pk)
        package.status = request.data['status']
        package.save()
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
    
class PackageItemGET(APIView):
    def get_object(self, pk):
        try:
            return PackageItem.objects.filter(package_id=pk)
        except PackageItem.DoesNotExist:
            raise 404
        
    def get(self, request, pk):
        packages = self.get_object(pk)
        print(packages, 'packages')
        data = []
        if len(packages) != 0:
            for i in packages:
                serializer = PackageItemSerializer(i)
                data.append(serializer.data)
        # serializer = PackageItemSerializer(packages[0])
        return Response(data)    
    
    def put(self, request, pk):
        toppings = ItemTopping.objects.filter(item_id=pk)
        for i in toppings:
            i.delete()
        package = PackageItem.objects.get(id=pk).delete()
        return Response('deleted')
    
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
    
class ItemToppingGET(APIView):
    def get_object(self, pk):
        data = []
        try:
            packages = PackageItem.objects.filter(package_id=pk)
            for i in packages:
                item = ItemTopping.objects.get(item_id=i.id)
                data.append(item)
            return data
        except ItemTopping.DoesNotExist:
            raise 404
        
    def get(self, request, pk):
        item_topping = self.get_object(pk)
        data = []
        if len(item_topping) != 0:
            for i in item_topping:
                serializer = ItemToppingSerializer(i)
                data.append(serializer.data)
        return Response(data)   
    
class RewardAPI(APIView):
    def get_object(self, pk):
        try:
            return Rewards.objects.get(id=pk)
        except Rewards.DoesNotExist:
            raise 404
        
    def get(self, request):
        reward = Rewards.objects.all()
        serializer = RewardsSerializer(reward, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        reward = Rewards.objects.get(id=request.data['id'])
        serializer = RewardsSerializer(reward, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def post(self, request):
        serializer = RewardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class RewardGET(APIView):
    def get_object(self, pk):
        data = []
        try:
            return Rewards.objects.get(id=pk)
        except Rewards.DoesNotExist:
            raise 404
        
    def get(self, request, pk):
        reward = self.get_object(pk)
        serializer = RewardsSerializer(reward)
        return Response(serializer.data)   
    
    def put(self, request, pk):
        reward = self.get_object(pk)
        reward.status = request.data['status']
        reward.save()
        serializer = RewardsSerializer(reward)
        return Response(serializer.data)
    
class ConditionRewardAPI(APIView):
    def get_object(self, pk):
        try:
            return ConditionRewards.objects.get(id=pk)
        except ConditionRewards.DoesNotExist:
            raise 404
        
    def get(self, request):
        reward = ConditionRewards.objects.all()
        serializer = ConditionRewardsSerializer(reward, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        reward = ConditionRewards.objects.get(id=request.data['id'])
        serializer = ConditionRewardsSerializer(reward, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def post(self, request):
        serializer = ConditionRewardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class ConditionRewardGET(APIView):
    def get_object(self, pk):
        try:
            return ConditionRewards.objects.filter(reward_id=pk)
        except ConditionRewards.DoesNotExist:
            raise 404
        
    def get(self, request, pk):
        rewards = self.get_object(pk)
        print(rewards)
        data = []
        if len(rewards) != 0:
            for i in rewards:
                serializer = ConditionRewardsSerializer(i)
                data.append(serializer.data)
        return Response(data)   
    
    def put(self, request, pk):
        ConditionRewards.objects.get(id=pk).delete()
        return Response('deleted')
    
class CustomerPointAPI(APIView):
    def get_object(self, pk):
        try:
            return CustomerPoint.objects.get(customer_id=pk)
        except CustomerPoint.DoesNotExist:
            raise 404
        
    def get(self, request):
        cus_point = CustomerPoint.objects.all()
        serializer = CustomerPointSerializer(cus_point, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        cus_point = CustomerPoint.objects.get(id=request.data['id'])
        serializer = CustomerPointSerializer(cus_point, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def post(self, request):
        serializer = CustomerPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
class CustomerPointGET(APIView):
    def get_object(self, pk):
        try:
            return CustomerPoint.objects.filter(customer_id=pk)
        except CustomerPoint.DoesNotExist:
            raise 404
        
    def get(self, request, pk):
        cus_points = self.get_object(pk)
        print(cus_points)
        data = []
        if len(cus_points) != 0:
            for i in cus_points:
                serializer = CustomerPointSerializer(i)
                data.append(serializer.data)
        return Response(data)   
    
class CustomerPointAPI(APIView):
    def get_object(self, pk):
        try:
            return CustomerPoint.objects.get(customer_id=pk)
        except CustomerPoint.DoesNotExist:
            raise 404
        
    def get(self, request):
        cus_point = CustomerPoint.objects.all()
        serializer = CustomerPointSerializer(cus_point, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        cus_point = CustomerPoint.objects.get(id=request.data['id'])
        serializer = CustomerPointSerializer(cus_point, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def post(self, request):
        serializer = CustomerPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
class ExchangeHistoryAPI(APIView):
    def get_object(self, pk):
        try:
            return ExchangeHistory.objects.get(customer_id=pk)
        except ExchangeHistory.DoesNotExist:
            raise 404
        
    def get(self, request):
        exchange_history = ExchangeHistory.objects.all()
        serializer = ExchangeHistorySerializer(exchange_history, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        exchange_history = ExchangeHistory.objects.get(id=request.data['id'])
        serializer = ExchangeHistorySerializer(exchange_history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def post(self, request):
        serializer = ExchangeHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
class ExchangeHistoryGET(APIView):
    def get_object(self, pk):
        try:
            return ExchangeHistory.objects.filter(customer_id=pk)
        except ExchangeHistory.DoesNotExist:
            raise 404
        
    def get(self, request, pk):
        exchange_histories = self.get_object(pk)
        print(exchange_histories)
        data = []
        if len(exchange_histories) != 0:
            for i in exchange_histories:
                serializer = ExchangeHistorySerializer(i)
                data.append(serializer.data)
        return Response(data)   
    
    
class DBS(APIView):
    def get(self, request):
        with open("dbs.txt", "r") as data:
            dictionary = ast.literal_eval(data.read())
        print(dictionary['change'], 'read')
        return Response(dictionary)   
    
    def post(self, request):
        my_file = open("dbs.txt", "w")
        data = repr(request.data)
        my_file.write(data)
        my_file.close()
        print(request.data, 'data')
        return Response('good')