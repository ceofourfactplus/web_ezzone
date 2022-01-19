from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.serializers import CustomerSerializer
from customer.models import Customer,AddressCustomer
import datetime
from rest_framework.parsers import FormParser, MultiPartParser

# Create your views here.

class GetCustomerByPhoneNumbe(APIView):
    def get(self,request,phone_number):
        customer = Customer.objects.filter(phone_number__contains=phone_number)
        serializer = CustomerSerializer(customer,many=True)
        return Response(serializer.data,status=200)

class CustomerList (APIView):
    # parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(
            customer, context={'request':request},many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data['id'])
            AddressCustomer.objects.create(
                address = request.data['address'],
                customer_id = serializer.data['id'],
                status_address = 1,
            )
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CustomerDetail(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise 404

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, context={"request": request})
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        customer = self.get_object(pk)
        print(request.data)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class SaveAddress(APIView):

    def put(self, request, pk):
        customer = AddressCustomer.objects.get(pk=pk)
        customer.address = request.data['address']
        customer.save()
        print(customer.address)
        return Response('ok')

class CreateAddress(APIView):
    def put(self, request):
        AddressCustomer.objects.create(
                address = request.data['address'],
                customer_id = request.data['customer_id'],
                status_address = 1,
            )
        return Response('ok')

class SearchName (APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, text):
        customer = Customer.objects.filter(nick_name__contains=text)
        serializer = CustomerSerializer(
            customer, context={"request": request}, many=True)
        return Response(serializer.data, status=200)
