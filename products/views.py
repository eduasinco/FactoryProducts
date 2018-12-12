from products.serializers import *
from products.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductList(APIView):

    def get(self, request):
        factory_name = request.META['HTTP_X_API_KEY']
        products = Product.objects.using(factory_name)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        factory_name = request.META['HTTP_X_API_KEY']
        data = {}
        for k in request.data:
            data[k] = request.data[k]
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save(using=factory_name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
