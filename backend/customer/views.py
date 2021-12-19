from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.serializers import CustomerSerializer
from customer.models import Customer
from rest_framework.parsers import FormParser, MultiPartParser

# Create your views here.


class CustomerList (APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(
            customer, context={"request": request}, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CustomerDetail(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise 404

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class SaveAddress(APIView):

    def put(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        customer.address = request.data['address']
        customer.save()
        return Response('ok')
